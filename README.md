# meter-reading-python

Demonstration Python scripts to process, analyse, and report utility meter reading data.

## Overview

This project processes meter reading data from a JSON file and outputs a formatted text file containing meter readings.

## Features

- Reads meter data from `meterData.json`.
- Outputs a `reading.dat` file containing:
    1. A UNIX-friendly timestamp in `YYYY-MM-DD HH:MM:SS` format.
    2. Each `meter_id` and `new_reading` on separate lines.
- Handles missing `new_reading` values by writing an empty line instead of "None".
- Includes exception handling for file and JSON errors.

## Usage

Run the script using:

```bash
python export.py
```

### Expected Output

The `readings.dat` file will contain data in the following format:

```plaintext
2025-03-12 14:30:15
MT789123
1608
MT456789

```

## Dependencies

- Python 3.x
- No additional dependencies required (uses built-in libraries)

## Author

- **Steven Thompson** - March 12, 2025

