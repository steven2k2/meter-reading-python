-- SQL Script generated on 2025-03-12 19:05:18

DROP DATABASE IF EXISTS meter_reading;
CREATE DATABASE meter_reading;
USE meter_reading;

CREATE TABLE meter_data (
    meter_id TEXT,
    new_reading TEXT,
    previous_reading TEXT,
    balance_due TEXT,
    application_status TEXT,
    address_1 TEXT,
    address_2 TEXT,
    address_3 TEXT,
    address_4 TEXT
);

INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('1', '45 Fjordveien', 'Hus B', 'Sentrum', 'Oslo, NO-0250', 'Approved', '67.89', 'BMK56789', 'B002');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('CONN789123', 'Possible pipe issue, check for moisture', '28', '7', '980', '2', '18.75', 'HK002', '27');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Gnr 124, Bnr 5', 'Bakke residential area', '12 Elvegata', 'Local 5', 'Type B, Model Y', 'MT789123', 'Backyard', 'Under stairs', 'Basement');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Easy access', 'Access requires a code', '2 inch', 'Analog', '1.30', 'Ola Nordmann', 'Kari Nordmann', '1608', '1580');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('180', 'R567890', 'SEQ234', 'RK123789', '2.5 inch', '2024-03-05', 'Regular', 'Active', '12.50');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('3', 'O.N.', 'Standard', 'Regular residential tariff', 'Fjord Utilities', '2024-03-05T14:40:00Z', 'UA456', 'VN78901', '5');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('78 Kystveien', 'Apt. 302', 'Bryggen', 'Bergen, NO-5003', 'Pending', '32.45', 'BMK67890', 'B003', 'CONN456789');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Possible leakage in basement, inspect water stains', '31', '5', '1350', '4', '20.00', 'HK003', '30', 'Gnr 78, Bnr 12');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Bryggen residential complex', '99 Fjelltunet', 'House 8', 'Type C, Model Z', 'MT456789', 'Garage', 'Rooftop terrace', 'Behind stairs', 'Difficult access');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Special key required', '1 inch', 'Smart', '1.15', 'Erik Hansen', 'Lise Berg', NULL, '1370', '130');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('R234567', 'SEQ567', 'RK345678', '1.75 inch', '2024-03-05', 'Emergency', 'Pending', '9.50', '1');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('E.H.', 'Small household', 'Apartment residential tariff', 'Vest Utilities', '2024-03-05T14:50:00Z', 'UA789', 'VN23456', '10', '23 Havnegata');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Leilighet 12B', 'Strandkanten', 'Trondheim, NO-7010', 'Approved', '78.25', 'BMK12345', 'B004', 'CONN112233', 'Water pressure slightly inconsistent, monitor usage');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('30', '6', '1150', '3', '22.00', 'HK004', '29', 'Gnr 200, Bnr 15', 'Strandkanten residential area');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('10 Nidelvgata', 'Suite 5', 'Type A, Model X', 'MT112233', 'Laundry room', 'Under sink', 'Utility closet', 'Easily accessible', 'Access via rear entrance');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('1.5 inch', 'Digital', '1.20', 'Jens Løvik', 'Mona Sæther', '1905', '1855', '150', 'R123456');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('SEQ678', 'RK678901', '2.0 inch', '2024-03-06', 'Routine', 'Active', '14.75', '2', 'J.L.');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Standard', 'Regular residential tariff', 'Trøndelag Vann', '2024-03-06T10:30:00Z', 'UA567', 'VN56789', '15', '89 Solbergveien', 'Villa A');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Solberg', 'Stavanger, NO-4008', 'Pending', '45.9', 'BMK34567', 'B005', 'CONN998877', 'Meter box slightly rusted, consider maintenance', '32');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('5', '890', '1', '19.50', 'HK005', '31', 'Gnr 321, Bnr 10', 'Solberg suburban district', '15 Løkkeveien');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Building 3', 'Type B, Model W', 'MT998877', 'Outdoor shed', 'Garage wall', 'Driveway corner', 'Requires a ladder for access', 'Keypad lock present', '2 inch');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Analog', '1.10', 'Henrik Olsen', 'Siri Eide', NULL, '1725', '135', 'R998877', 'SEQ789');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('RK567234', '2.25 inch', '2024-03-07', 'Emergency', 'Pending', '10.25', '3', 'H.O.', 'Suburban household');
INSERT INTO meter_data (meter_id, new_reading, previous_reading, balance_due, application_status, address_1, address_2, address_3, address_4) VALUES ('Standard residential tariff', 'Rogaland Vann & Energi', '2024-03-07T12:15:00Z', 'UA890', 'VN34567');
