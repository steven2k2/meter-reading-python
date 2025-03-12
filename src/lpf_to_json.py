import json
from datetime import datetime

"""
lpf-to-json.py

This utility reads a line-per-field (LPF) file and converts it back into JSON format.
The LPF format is an intermediate representation used for migrating data from a
COBOL-based utility billing system.

Each record in the LPF file follows a fixed field order.

Note: Automatic type conversion has been implemented for better data integrity.
"""

# Input and output file paths
input_file = "../data/readings.lpf"
output_json_file = "../output/readings.json"

# Define field order (must match original JSON structure)
FIELDS = [
    "id",
    "address_1",
    "address_2",
    "address_3",
    "address_4",
    "application_status",
    "balance_due",
    "bookmark",
    "book_no",
    "connection_id",
    "consumer_meter_reader_note",
    "days",
    "dials",
    "estimated_units",
    "estimates_count",
    "fixed_charges",
    "house_key",
    "last_days",
    "legal_description_1",
    "legal_description_2",
    "location_address_1",
    "location_address_2",
    "meter_detail",
    "meter_id",
    "meter_location_01",
    "meter_location_02",
    "meter_location_03",
    "meter_reader_note",
    "meter_reader_note_2",
    "meter_size",
    "meter_type",
    "multiplier",
    "name_1",
    "name_2",
    "new_reading",
    "previous_reading",
    "previous_units",
    "rapid_no",
    "read_sequence",
    "record_key",
    "restrictor_size",
    "special_read_date",
    "special_read_type",
    "status",
    "supply_charges",
    "supply_tariff",
    "surname_initials",
    "tariff",
    "tariff_description",
    "trade_name",
    "update_time",
    "user_alpha_01",
    "valuation_number_01",
]


def parse_text(value):
    """Trims unnecessary whitespace from text fields."""
    return value.strip() if value else None


def parse_date(value, fmt="%Y-%m-%d"):
    """Parses a date string into the specified format."""
    try:
        return (
            datetime.strptime(value.strip(), fmt).strftime(fmt)
            if value.strip()
            else None
        )
    except ValueError:
        return value  # Return original value if parsing fails


# Define expected data types and custom parsers
FIELD_TYPES = {
    "id": int,
    "new_reading": lambda x: int(x) if x.isdigit() else None,
    "previous_reading": lambda x: int(x) if x.isdigit() else None,
    "balance_due": lambda x: float(x) if x.replace(".", "", 1).isdigit() else None,
    "days": int,
    "dials": int,
    "estimated_units": int,
    "estimates_count": int,
    "fixed_charges": lambda x: float(x) if x.replace(".", "", 1).isdigit() else None,
    "last_days": int,
    "multiplier": lambda x: float(x) if x.replace(".", "", 1).isdigit() else None,
    "previous_units": int,
    "supply_charges": lambda x: float(x) if x.replace(".", "", 1).isdigit() else None,
    "supply_tariff": int,
    "special_read_date": lambda x: parse_date(x, "%Y-%m-%d"),
    "update_time": lambda x: parse_date(x, "%Y-%m-%dT%H:%M:%SZ"),
    # Use parse_text for trimming unnecessary whitespace
    "meter_location_01": parse_text,
    "meter_location_02": parse_text,
    "meter_location_03": parse_text,
    "meter_reader_note": parse_text,
    "meter_reader_note_2": parse_text,
}


def convert_value(field, value):
    """Convert field value based on FIELD_TYPES mapping."""
    value = value.strip()
    if not value:
        return None  # Handle empty values
    try:
        return FIELD_TYPES[field](value) if field in FIELD_TYPES else value
    except ValueError:
        return value  # Fallback to string if conversion fails


def process_lpf_to_json():
    """Reads LPF file and converts it to JSON."""
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        # The first line is a timestamp, so we ignore it
        lines = lines[1:]

        # Ensure the number of lines is a multiple of the number of fields
        if len(lines) % len(FIELDS) != 0:
            raise ValueError(
                "Invalid LPF format: Number of lines does not match expected field count."
            )

        # Process records (each record has len(FIELDS) lines)
        records = [
            {
                FIELDS[i]: convert_value(FIELDS[i], lines[j + i])
                for i in range(len(FIELDS))
            }
            for j in range(0, len(lines), len(FIELDS))
        ]

        # Convert to JSON format
        json_output = {"meterData": records}
        with open(output_json_file, "w", encoding="utf-8") as json_file:
            json.dump(json_output, json_file, indent=4)

        print(f"Successfully converted LPF to JSON: {output_json_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    process_lpf_to_json()
