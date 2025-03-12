### Adding API Functionality to the Meter Reading Project

#### 1. Install FastAPI & Uvicorn
```bash
pip install fastapi uvicorn
```

#### 2. Create `api.py`
This script exposes API endpoints for:
- Fetching meter readings
- Converting JSON to LPF
- Converting LPF to JSON
- Uploading LPF files
- Inserting LPF data into MySQL

```python
from fastapi import FastAPI, File, UploadFile
import json
import subprocess
from pathlib import Path
from lpf_to_json import process_lpf_to_json  # Import conversion function

app = FastAPI()
DATA_DIR = Path("./data")

@app.get("/")
def home():
    return {"message": "Meter Reading API is running"}

@app.get("/readings")
def get_readings():
    """Returns meter data as JSON."""
    json_file = DATA_DIR / "meterData.json"
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {"error": "Meter data file not found"}

@app.post("/convert/json-to-lpf")
def json_to_lpf():
    """Converts JSON meter data to LPF format."""
    try:
        subprocess.run(["python", "json-to-lpf.py"], check=True)
        return {"message": "Conversion successful", "output": "reading.lpf"}
    except subprocess.CalledProcessError:
        return {"error": "Conversion failed"}

@app.post("/convert/lpf-to-json")
def lpf_to_json():
    """Converts LPF format to JSON."""
    try:
        process_lpf_to_json()
        return {"message": "Conversion successful", "output": "meterData_converted.json"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/upload-lpf")
async def upload_lpf(file: UploadFile = File(...)):
    """Uploads an LPF file and processes it."""
    file_location = DATA_DIR / file.filename
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    return {"message": f"File '{file.filename}' uploaded successfully"}

@app.post("/insert/mysql")
def insert_mysql():
    """Processes LPF data and inserts into MySQL."""
    try:
        subprocess.run(["python", "lpf-to-mysql.py"], check=True)
        return {"message": "Data inserted into MySQL successfully"}
    except subprocess.CalledProcessError:
        return {"error": "Database insert failed"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### 3. Run the API
```bash
uvicorn api:app --reload
```

#### 4. Test API Endpoints
- **Get meter readings (JSON)**
  ```bash
  curl http://127.0.0.1:8000/readings
  ```
- **Convert JSON to LPF**
  ```bash
  curl -X POST http://127.0.0.1:8000/convert/json-to-lpf
  ```
- **Convert LPF to JSON**
  ```bash
  curl -X POST http://127.0.0.1:8000/convert/lpf-to-json
  ```
- **Insert LPF data into MySQL**
  ```bash
  curl -X POST http://127.0.0.1:8000/insert/mysql
  ```
  
