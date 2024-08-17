import os
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("Healthcare ETL").getOrCreate()

# Reading from a CSV file into Spark DataFrame
df = spark.read.csv('Healthcare_Associated_Infections-Hospital.csv', header=True, inferSchema=True)

# Display the first few rows to verify the data
df.show()

output_path = 'output_data/output.csv'

# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write the processed DataFrame to a CSV file
df.write.csv(output_path, header=True)

# Stop the Spark session
spark.stop()
