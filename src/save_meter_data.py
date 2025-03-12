import json
from pathlib import Path
from datetime import datetime

data_dir = Path("./data")
data_dir.mkdir(exist_ok=True)  # Ensure the data directory exists

def save_meter_data(data):
    """Saves the provided meter data to a timestamped JSON file."""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = data_dir / f"meterData_{timestamp}.json"

        with file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return {"success": True, "message": f"Data saved to {file_path}"}
    except Exception as e:
        return {"success": False, "message": f"Error saving data: {str(e)}"}
