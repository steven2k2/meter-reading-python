import json

# Load meter reading data from the JSON file
with open('./data/meterData.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

meter_readings = data['meterData']

# Loop through each meter record and print key details
for meter in meter_readings:
    name = f"{meter['name_1']} ({meter['surname_initials']})"
    address = f"{meter['address_1']}, {meter.get('address_2', '')}, {meter.get('address_4')}"
    meter_id = meter['meter_id']
    status = meter['application_status']
    balance_due = meter['balance_due']

    print(f"Meter ID: {meter_id}")
    print(f"Customer: {name}")
    print(f"Address: {address}")
    print(f"Status: {status}")
    print(f"Balance Due: ${balance_due:.2f}")
    print("-" * 40)