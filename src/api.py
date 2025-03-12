from fastapi import FastAPI, HTTPException, Body
from typing import List, Dict
from src.get_meter_data import get_meter_data  # Updated import
from src.save_meter_data import save_meter_data  # Import save function

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI running"}

@app.get("/meter-data")
def meter_data_endpoint():
    """Calls the meter data function and returns the result."""
    try:
        response = get_meter_data()
        if not response.get("success"):
            raise HTTPException(status_code=400, detail=response.get("message"))
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/meter-readings")
def save_meter_readings(data: List[Dict] = Body(...)):
    """Receives meter readings (single or bulk) and saves them."""
    try:
        response = save_meter_data(data)
        if not response.get("success"):
            raise HTTPException(status_code=400, detail=response.get("message"))
        return {
            "success": response.get("success"),
            "message": response.get("message"),
            "total": len(data),
            "data": response.get("data")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))