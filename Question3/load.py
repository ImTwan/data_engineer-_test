# load.py for PostgreSQL
import psycopg2
import json

# Connection details (change as needed)
DB_HOST = "PG Local"
DB_NAME = "demo"
DB_USER = "postgres"
DB_PASS = "Tuan@2592003"
DB_PORT = "5433"

INPUT_JSON = "employees_transformed.json"

def load(data):
    """Insert transformed data into PostgreSQL."""
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Insert each record
        for record in data:
            cursor.execute("""
                INSERT INTO employees (employees_id, employees_name, department, salary, join_date)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (employees_id) DO UPDATE 
                SET employees_name = EXCLUDED.employees_name,
                    department = EXCLUDED.department,
                    salary = EXCLUDED.salary,
                    join_date = EXCLUDED.join_date
            """, (
                record["id"], record["name"], record["department"],
                record["salary"], record["join_date"]
            ))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data loaded into PostgreSQL successfully!")
    except Exception as e:
        print(f"Error loading data: {e}")

# Read transformed JSON
with open(INPUT_JSON, "r", encoding="utf-8") as f:
    transformed_data = json.load(f)

load(transformed_data)
