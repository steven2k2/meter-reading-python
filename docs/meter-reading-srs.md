# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for a Utility Meter Reading Application. The application manages meter reading data, provides APIs for data handling, and supports accurate billing, customer management, and maintenance processes.

### 1.2 Scope
This project focuses on processing, analysing, and reporting meter readings, handling data storage, and providing API endpoints for frontend or other external applications.

## 2. Functional Requirements

### 2.1 Meter Data Management
- **FR-01**: The system must read meter data from JSON files.
- **FR-02**: The system should save meter data in timestamped files for auditing.
- **FR-03** Support JSON and Line-Per-Field (LPF) data formats.

### 2.2 API Endpoints
- **FR 2.2.1 GET /meter-data**: Retrieve meter data in structured format.
- **FR 2.2.2 POST /meter-readings**: Accept single or multiple meter readings and save data with structured responses.

### 2.3 Customer and User Interaction
- **FR 2.3.1** Store and retrieve customer feedback and service requests.

### 2.4 Error and Exception Handling
- Robust error handling with descriptive and structured API responses.

## 3. Data Requirements

### 3.1 Customer Information
- Customer ID
- Full Name
- Contact Details (phone, email, mailing address)

### 3.2 Meter Information
- Meter ID
- Meter Type (Analog, Digital, Smart)
- Installation Date
- Location (Physical placement)

### 3.3 Meter Reading Information
- Reading Timestamp
- Consumption Reading
- Units of Measurement
- Previous Reading
- Estimated Usage

### 3.4 Billing Information
- Billing Period (start and end)
- Tariff Details
- Fixed Charges
- Consumption Charges
- Payment Status (Paid, Pending, Overdue)

### 3.4 Maintenance and Logs
- Last Communication Timestamp
- Signal Strength
- Error Logs
- Maintenance Records

### 3.5 Regulatory and Compliance
- Data audit trails
- Secure data handling and storage

## 4. Non-Functional Requirements

### 4.1 Performance
- API response time should be under 500 ms per request.
- The System must handle bulk data efficiently.

### 4.2 Security
- Ensure secure API endpoints (HTTPS recommended).
- Validate all input data to prevent security vulnerabilities (injection attacks, etc.).

### 4.3 Maintainability
- Code must adhere to PEP8 standards.
- Project must use automated formatting (Black).
- Clearly documented functions and modules.

### 4.4 Reliability
- Robust error handling for file I/O and data parsing.
- Regular backups of meter data.

### 4.5 Performance
- Efficient handling of multiple concurrent API requests.

## 5. Project Structure

```plaintext
meter-reading-python/
├── data/                  # Sample JSON files and saved meter data
├── src/                   # Core Python scripts
│   ├── meter_reader.py
│   ├── export.py
│   ├── json-to-lpf.py
│   ├── lpf-to-json.py
│   ├── lpf-to-mysql.py
│   ├── get_meter_data.py
│   ├── save_meter_data.py
│   └── utils.py
├── tests/                 # Unit tests
├── README.md
├── .gitignore

## 5.1 Dependencies
- Python 3.x
- FastAPI
- Uvicorn
- JSON handling (built-in)
- Requests (for testing API)
- Black (code formatter)

## 5. API Data Format

- JSON structured responses:
  ```json
  {
    "success": true,
    "total": 2,
    "data": [
      {
        "meter_id": "MT123456",
        "reading": 1200,
        "timestamp": "2025-03-12T14:30:00Z"
      }
    ]
  }
  ```

## 6. Acceptance Criteria
- API endpoints tested and verified with standard HTTP responses (200, 400, 500).
- JSON data files are correctly handled and validated.

## 7. Revision History
| Date       | Author          | Version | Description                    |
|------------|-----------------|---------|--------------------------------|
| 2025-03-12 | Steven Thompson | 1.0     | Initial specification creation |

## Author
- **Steven Thompson**

## 8. References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Black formatter](https://black.readthedocs.io/en/stable/)

</content>

