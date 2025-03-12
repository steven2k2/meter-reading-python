# Meter data schema

This document provides an overview of the fields used in the **UtilityTrak Reading System**, including their purpose and expected data format.

## **Fields and Descriptions**

| Field Name                   | Data Type  | Description                                                        |
|------------------------------|------------|--------------------------------------------------------------------|
| `record_id`                  | `string`   | Unique identifier for each meter reading record.                   |
| `address_1`                  | `string`   | Primary address of the meter location.                             |
| `address_2`                  | `string`   | Secondary address details, such as unit or apartment number.       |
| `address_3`                  | `string`   | Additional location information (if applicable).                   |
| `address_4`                  | `string`   | Additional address details (city, region, etc.).                   |
| `application_status`         | `string`   | Status of the application (e.g., Pending, Approved).               |
| `billing_balance_due`        | `decimal`  | The total amount due on the meter account.                         |
| `bookmark`                   | `string`   | A reference bookmark for the meter reading.                        |
| `book_no`                    | `string`   | The book number where this meter is recorded.                      |
| `connection_id`              | `string`   | Unique identifier for the connection.                              |
| `consumer_meter_reader_note` | `string`   | Notes recorded by the meter reader regarding the consumer's meter. |
| `days`                       | `integer`  | The number of days since the last meter reading.                   |
| `dials`                      | `integer`  | The number of dials on the meter.                                  |
| `estimated_units`            | `integer`  | The estimated usage in units.                                      |
| `estimates_count`            | `integer`  | The number of times the meter reading has been estimated.          |
| `billing_fixed_charges`      | `decimal`  | Fixed charges applicable to the meter connection.                  |
| `house_key`                  | `string`   | A reference to the key used for meter access.                      |
| `last_days`                  | `integer`  | The number of days covered by the last billing cycle.              |
| `legal_description_1`        | `string`   | Legal description of the property where the meter is installed.    |
| `legal_description_2`        | `string`   | Additional legal property details.                                 |
| `location_address_1`         | `string`   | The specific location where the meter is installed.                |
| `location_address_2`         | `string`   | Additional meter location details.                                 |
| `meter_detail`               | `string`   | Technical details of the meter type and model.                     |
| `meter_id`                   | `string`   | Unique identifier assigned to the meter.                           |
| `meter_location_1`           | `string`   | Primary meter location description.                                |
| `meter_location_2`           | `string`   | Secondary meter location description.                              |
| `meter_location_3`           | `string`   | Tertiary meter location description.                               |
| `meter_reader_note`          | `string`   | Notes added by the meter reader regarding the meter.               |
| `meter_reader_note_2`        | `string`   | Additional meter reader notes.                                     |
| `meter_size`                 | `string`   | The physical size of the meter (e.g., 2 inches).                   |
| `meter_type`                 | `string`   | The type of meter (e.g., Analog, Digital).                         |
| `multiplier`                 | `decimal`  | The multiplier applied to the meter reading.                       |
| `name_1`                     | `string`   | Primary account holder’s name.                                     |
| `name_2`                     | `string`   | Secondary account holder’s name.                                   |
| `new_reading`                | `integer`  | The latest recorded meter reading.                                 |
| `previous_reading`           | `integer`  | The previous recorded meter reading.                               |
| `previous_units`             | `integer`  | The number of units used since the last reading.                   |
| `rapid_no`                   | `string`   | Rapid identification number for emergency readings.                |
| `read_sequence`              | `string`   | The sequence in which the meter should be read.                    |
| `record_key`                 | `string`   | A unique key identifying this record in the system.                |
| `restrictor_size`            | `string`   | The size of any flow restrictor installed.                         |
| `special_read_date`          | `date`     | Date of a special meter reading request.                           |
| `special_read_type`          | `string`   | Type of special reading requested (e.g., Emergency).               |
| `meter_status`               | `string`   | The current status of the meter (e.g., Active, Inactive).          |
| `billing_supply_charges`     | `decimal`  | Charges associated with the supply of utility services.            |
| `supply_tariff`              | `integer`  | The tariff category applied to the supply.                         |
| `surname_initials`           | `string`   | Initials of the primary account holder.                            |
| `tariff`                     | `string`   | The applicable tariff category.                                    |
| `tariff_description`         | `string`   | Description of the tariff being applied.                           |
| `trade_name`                 | `string`   | The trading name associated with the account.                      |
| `update_timestamp`           | `datetime` | The last time this record was updated.                             |
| `user_alpha_1`               | `string`   | Custom user-defined field.                                         |
| `valuation_number_1`         | `string`   | The valuation number assigned to the property.                     |

## **Data Format Considerations**
- **String fields** should be trimmed to remove leading/trailing spaces.
- **Integer fields** should default to `0` if missing.
- **Decimal fields** should store amounts with two decimal places for currency values.
- **Date fields** should use `YYYY-MM-DD` format.
- **Datetime fields** should use `YYYY-MM-DD HH:MM:SS` format and be stored in UTC.

---
This document serves as a reference for developers and database administrators working with meter reading data.

---

# Utility Meter Reading App Data Requirements

This document summarises the typical data fields required by a utility meter reading application.

## Customer Information
- **customer_id**: Unique customer identifier.
- **name**: Full name of account holder(s).
- **contact_details**: Phone number, email address, mailing address.

## Meter Details
- **meter_id**: Unique identifier for each meter.
- **meter_type**: Type (e.g., analog, digital, smart).
- **installation_date**: Date of meter installation.
- **location**: Physical location on property.
- **meter_size**: Size of the meter.
- **meter_status**: Current status (active/inactive).

## Consumption Data
- **previous_reading**: Last recorded reading.
- **new_reading**: Latest meter reading.
- **timestamp**: Date and time of the current reading.
- **units**: Units (e.g. kWh, cubic meters).

## Billing Information
- **billing_period**: Start and end date of billing cycle.
- **tariff**: Rate or tariff description.
- **fixed_charges**: Fixed fees per billing cycle.
- **supply_charges**: Charges based on consumption.
- **balance_due**: Total amount outstanding.
- **payment_status**: Paid, pending, overdue.

## Maintenance Records
- **last_maintenance_date**: Date of last maintenance activity.
- **maintenance_notes**: Notes detailing maintenance activities performed.

## Communication and Errors
- **last_communication**: Last successful data transmission timestamp.
- **signal_strength**: Quality indicator for meter signal.
- **error_logs**: Errors encountered during transmission or reading.

## Customer and User Interaction
- **customer_feedback**: Notes or comments from customers.
- **service_requests**: Records of maintenance or inspection requests.

## Regulatory and Audit
- **legal_description**: Legal property description.
- **update_timestamp**: Timestamp of last data update or record modification.
