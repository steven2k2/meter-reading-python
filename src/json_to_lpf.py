import json
from datetime import datetime

"""
json-to-lpf.py

This utility processes JSON meter data that simulates the data held in a legacy COBOL utility billing system.
The output is a line-per-field intermediate format that will be further processed or converted into another format.
Each field is written on a separate line, and null values are replaced with empty lines.
"""

# Input and output file paths
json_file = "../data/meterData.json"
output_file = "../output/readings.lpf"

try:
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    meter_readings = data.get("meterData", [])

    with open(output_file, "w", encoding="utf-8") as outfile:
        # Write a UNIX-friendly timestamp as the first line
        outfile.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for meter in meter_readings:
            for key, value in meter.items():
                outfile.write(f"{'' if value is None else value}\n")

    print(f"Successfully written meter readings to {output_file}")

except FileNotFoundError:
    print(f"Error: {json_file} not found.")
except json.JSONDecodeError:
    print(f"Error: Could not parse {json_file} as JSON.")
except Exception as e:
    print(f"Unexpected error: {e}")
