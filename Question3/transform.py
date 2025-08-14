from datetime import datetime
import json

json_file = 'D:\python try hard\DE\data_engineer-_test\Question3\employees.json'  # JSON file path
output_file = 'transformed_employees.json'  # Output file path

def transform(data):
    transformed_data = []
    for record in data:
        try:
            # Convert join_date to datetime object
            join_date = datetime.strptime(record['join_date'], '%Y-%m-%d')
            # Create a new record with transformed fields
            transformed_record = {
                'id': record['id'],
                'name': record['name'],
                'department': record['department'],
                'salary': record['salary'],
                'join_date': join_date.strftime('%Y-%m-%d')  # Format back to string if needed
            }
            transformed_data.append(transformed_record)
        except (ValueError, KeyError) as e:
            print(f"Error processing record: {e}")
    return transformed_data

with open (json_file, 'r') as file:
    raw_data = json.load(file)

transformed_data = transform(raw_data)

with open(output_file, 'w') as file:
    json.dump(transformed_data, file, indent=4)

print(f"Transformed data saved to {output_file}")