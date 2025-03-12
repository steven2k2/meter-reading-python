import datetime

"""
lpf-to-mysql.py

This utility reads a line-per-field (LPF) file generated from the JSON meter data
and generates an SQL script that:
1. Drops the existing database (if it exists)
2. Creates a new database
3. Creates a table
4. Inserts the data from the LPF file

The output is a self-contained SQL script that can be executed in MySQL.
"""

# Input file
input_file = "../data/readings.lpf"
output_sql_file = "../output/setup_meter_data.sql"

# Database and table details
DB_NAME = "meter_reading"
TABLE_NAME = "meter_data"
FIELDS = [
    "meter_id",
    "new_reading",
    "previous_reading",
    "balance_due",
    "application_status",
    "address_1",
    "address_2",
    "address_3",
    "address_4",
]

try:
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # The first line is a timestamp, so we ignore it
    lines = lines[1:]

    # Process records (each record has len(FIELDS) lines)
    record_size = len(FIELDS)
    records = [lines[i : i + record_size] for i in range(0, len(lines), record_size)]

    # Generate SQL script
    with open(output_sql_file, "w", encoding="utf-8") as sql_file:
        sql_file.write(
            f"-- SQL Script generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )
        sql_file.write(f"DROP DATABASE IF EXISTS {DB_NAME};\n")
        sql_file.write(f"CREATE DATABASE {DB_NAME};\n")
        sql_file.write(f"USE {DB_NAME};\n\n")

        # Create table
        sql_file.write(f"CREATE TABLE {TABLE_NAME} (\n")
        sql_file.write(",\n".join([f"    {field} TEXT" for field in FIELDS]))
        sql_file.write("\n);\n\n")

        # Insert records
        for record in records:
            values = [
                f"'{value.strip().replace("'", "''")}'" if value.strip() else "NULL"
                for value in record
            ]
            sql_file.write(
                f"INSERT INTO {TABLE_NAME} ({', '.join(FIELDS)}) VALUES ({', '.join(values)});\n"
            )

    print(f"Successfully generated SQL script: {output_sql_file}")

except FileNotFoundError:
    print(f"Error: {input_file} not found.")
except Exception as e:
    print(f"Unexpected error: {e}")
