import json
from pathlib import Path

METER_DATA_FILE = Path("./data/meterData.json")

def get_meter_data():
    """Reads and returns meter data in a structured server response."""
    try:
        # Check if the meter data file exists
        if not METER_DATA_FILE.exists():
            return {"success": False, "message": f"File {METER_DATA_FILE} not found"}

        # Open and load the JSON file
        with METER_DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        # Ensure 'meterData' exists and is a list to prevent unexpected errors
        meter_data = data.get("meterData", [])
        if not isinstance(meter_data, list):
            return {"success": False, "message": "Invalid data format: 'meterData' should be a list"}

        # Return the formatted response
        return {
            "success": True,
            "total": len(meter_data),  # Number of records
            "data": meter_data  # The actual meter data
        }
    except json.JSONDecodeError:
        # Handle invalid JSON format errors
        return {"success": False, "message": "Invalid JSON format"}
    except Exception as e:
        # Catch and return any other unexpected errors
        return {"success": False, "message": f"Unexpected error: {str(e)}"}