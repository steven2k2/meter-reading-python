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
│   ├── utils.py
├── tests/                 # Unit tests
├── README.md              # Project documentation
├── .gitignore
```

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
