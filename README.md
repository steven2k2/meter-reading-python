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

## Project Structure

```
meter-reading-python/
├── data/                  # Sample JSON files
├── src/                   # Core Python scripts
│   ├── meter_reader.py
│   ├── export.py
│   ├── json-to-lpf.py
│   ├── lpf-to-json.py
│   ├── lpf-to-mysql.py
│   ├── utils.py
├── tests/                 # Unit tests
├── README.md              # Project documentation
├── .gitignore
```

## Scripts

### `export.py`
Converts meter reading data from `meterData.json` into a structured text file (`reading.dat`).

### `json-to-lpf.py`
Reads meter data from `meterData.json` and converts it into a **line-per-field** (LPF) format, simulating legacy COBOL system output.

### `lpf-to-json.py`
Reads LPF-formatted data and converts it back into structured JSON format.

### `lpf-to-mysql.py`
Reads an LPF-formatted file and generates an SQL script that:
- Drops the existing database (if it exists).
- Creates a new database and table.
- Inserts the parsed data into the database.

### `meter_reading.py`
Utility script for handling meter reading logic and additional functionality.

### `format_code.sh`
A Bash script that runs **Black** to ensure PEP8-compliant formatting for all Python files in the project.

## Usage

Run the script using:

```bash
python export.py
```

### Expected Output

The `reading.dat` file will contain data in the following format:

```
2025-03-12 14:30:15
MT789123
1608
MT456789
```

## Dependencies

- Python 3.x
- No additional dependencies required (uses built-in libraries)

## Code Formatting with `black`

This project follows PEP8 standards for code formatting. To automatically format the Python scripts, install and use `black`:

### Install `black`
```bash
pip install black
```

### Format Code
```bash
black .
```
This will format all Python files in the project directory.

To check for formatting issues without modifying files:
```bash
black --check .
```

For consistency, it is recommended to run `black` before committing any changes.

## Author

- **Steven Thompson** - March 12, 2025

---

## Python Style Guide
This project follows the [Black](https://black.readthedocs.io/en/stable/) coding style.

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
