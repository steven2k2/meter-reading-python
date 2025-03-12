"""
export.py

This script reads meter reading data from 'meterData.json' and writes the meter_id
and new_reading values to 'reading.dat' in a line-per-field format.

Usage:
    python export.py

Output:
    - reading.dat: Contains meter readings in the format:
        UNIX_TIMESTAMP
        meter_id
        new_reading

Exceptions:
    - FileNotFoundError: Raised if 'meterData.json' is missing.
    - JSONDecodeError: Raised if 'meterData.json' is not properly formatted.
    - General Exception Handling: Catches unexpected errors.

Author:
    Steven Thompson

Date:
    March 12, 2025
"""

import json
import datetime

# Load the JSON data
json_file = "../data/meterData.json"
output_file = "readings.dat"

try:
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    meter_readings = data.get("meterData", [])

    # UNIX-friendly date (YYYY-MM-DD HH:MM:SS)
    unix_friendly_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open output file to write
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Write the UNIX-friendly timestamp as the first line
        outfile.write(f"{unix_friendly_date}\n")

        for meter in meter_readings:
            meter_id = meter.get("meter_id", "UNKNOWN")
            new_reading = meter.get("new_reading", "")

            # Ensure None values are written as empty lines
            if new_reading is None:
                new_reading = ""

            # Write meter_id and new_reading, each on a new line
            outfile.write(f"{meter_id}\n{new_reading}\n")

    print(f"Successfully written meter readings to {output_file}")

except FileNotFoundError:
    print(f"Error: {json_file} not found.")
except json.JSONDecodeError:
    print(f"Error: Could not parse {json_file} as JSON.")
except Exception as e:
    print(f"Unexpected error: {e}")
