import json
import pandas as pd
import sqlite3
from flask import Flask, jsonify
import requests

# 1. JSON DATA (Source)
# Raw JSON from an API or file
json_data = '''
[
    {"id": 1, "name": "Alice", "salary": 75000, "department": "Engineering"},
    {"id": 2, "name": "Bob", "salary": 65000, "department": "Sales"},
    {"id": 3, "name": "Charlie", "salary": 80000, "department": "Engineering"}
]
'''

# 2. JSON → PANDAS DATAFRAME
# Parse JSON and load into DataFrame for analysis
data = json.loads(json_data)
df = pd.DataFrame(data)
print("DataFrame from JSON:")
print(df)

# Data transformation in Pandas
df['salary_category'] = pd.cut(df['salary'], bins=[0, 70000, 100000], 
                                labels=['Standard', 'Premium'])

# 3. PANDAS → SQL TABLE 
# Store processed data in SQL database
conn = sqlite3.connect('employees.db')
df.to_sql('employees', conn, if_exists='replace', index=False)
print("\nData written to SQL table")

# 4. SQL → PANDAS (Query back) 
# Query from database when needed
query_df = pd.read_sql('SELECT * FROM employees WHERE department = "Engineering"', conn)
print("\nEngineering employees from SQL:")
print(query_df)

# 5. PANDAS → JSON (API Response)
# Convert back to JSON for API responses
json_response = df.to_json(orient='records')
print("\nJSON for API response:")
print(json_response)

# 6. API ENDPOINT
app = Flask(__name__)

@app.route('/api/employees', methods=['GET'])
def get_employees():
    """API serves data from SQL via Pandas"""
    df = pd.read_sql('SELECT * FROM employees', conn)
    return jsonify(df.to_dict(orient='records'))

# Clean up
conn.close()