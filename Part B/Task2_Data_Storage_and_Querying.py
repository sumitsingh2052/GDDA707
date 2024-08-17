from pymongo import MongoClient
import pandas as pd

# Load healthcare associated infections data
hai_df = pd.read_csv('Healthcare_Associated_Infections-Hospital.csv')

# Initialize MongoDB client
client = MongoClient('localhost', 27017)

# Access the database and collection on MongoDB Atlas
db = client['healthcare_db']
collection = db['infections']

# Insert data into MongoDB Atlas collection
data = hai_df.to_dict('records')
collection.insert_many(data)

# Query data from MongoDB, selecting specific fields for readability
results = collection.find({'Score': {'$gt': '1.0'}}, 
                          {'Facility Name': 1, 'State': 1, 'City/Town': 1, 
                           'Measure Name': 1, 'Score': 1, 'Compared to National': 1})

# Display results in a readable format
for result in results:
    print(f"Facility Name: {result.get('Facility Name')}")
    print(f"Location: {result.get('City/Town')}, {result.get('State')}")
    print(f"Measure: {result.get('Measure Name')}")
    print(f"Score: {result.get('Score')}")
    print(f"Compared to National Benchmark: {result.get('Compared to National')}")
    print("-" * 5)
