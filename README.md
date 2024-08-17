# Healthcare Data Engineering Project

## Overview

This project involves the development and implementation of a data engineering pipeline designed to integrate, process, and analyze healthcare datasets. The project is divided into two main parts:

1. **Part A: ETL Operations and Data Integration**
   - Focuses on extracting, transforming, and loading (ETL) data from various healthcare datasets, cleansing and preparing the data, and integrating it into a unified dataset for analysis.

2. **Part B: Big Data Analysis and Application of Engineering Techniques**
   - Involves applying big data techniques to ingest, store, and process large volumes of data, including real-time data clustering and data streaming for advanced analysis.

## Project Structure

```
Healthcare-Data-Engineering-Project/
│
├── PartA/
│   ├── Healthcare_Associated_Infections-Hospital.csv
│   ├── Hospital_General_Information.csv
│   ├── Task1_Load_and_Preprocessing.py
│   ├── Task2_ETL_and_Integration.py
│   └── README.md
│
├── PartB/
│   ├── Healthcare_Associated_Infections-Hospital.csv
│   ├── Hospital_General_Information.csv
│   ├── Task1_Data_Ingestion_Pipeline.py
│   ├── Task2_Data_Storage_and_Querying.py
│   ├── Task3_Real_Time_Data_Clustering.py
│   └── Task4_Data_Streaming_Pipeline.py
│
└── README.md
```

## Requirements

### Prerequisites

- **Python 3.x** - Programming language used for scripting.
- **Pandas** - Library for data manipulation and analysis.
- **PySpark** - Library for large-scale data processing.
- **MongoDB** - NoSQL database for storing and querying data.
- **Apache Kafka** - Distributed event streaming platform.
- **Apache NiFi** - Data integration tool (if applicable).
  
### Installation

1. **Clone the Repository:**

   ```bash
   git clone "project github link"
   cd Healthcare-Data-Engineering-Project
   ```

2. **Install Required Python Libraries:**

   ```bash
   pip install pandas pyspark pymongo kafka-python
   ```

3. **Ensure that MongoDB and Kafka are installed and running on your local machine:**

   - **MongoDB:** [Download and Install MongoDB](https://docs.mongodb.com/manual/installation/)
   - **Kafka:** [Download and Install Apache Kafka](https://kafka.apache.org/downloads)

4. **Set up Apache NiFi (if applicable):**

   - [Download and Install Apache NiFi](https://nifi.apache.org/download.html)

## Running the Project

### Part A: ETL Operations and Data Integration

1. **Task 1: Load and Pre-processing**

   - **Script:** `Task1_Load_and_Preprocessing.py`
   - **Description:** Loads healthcare datasets, performs data cleansing, and applies necessary transformations.
   - **Run Command:**

     ```bash
     python PartA/Task1_Load_and_Preprocessing.py
     ```

2. **Task 2: ETL Operations and Integration**

   - **Script:** `Task2_ETL_and_Integration.py`
   - **Description:** Integrates the cleansed datasets into a unified dataset using a common key.
   - **Run Command:**

     ```bash
     python PartA/Task2_ETL_and_Integration.py
     ```

### Part B: Big Data Analysis and Application of Engineering Techniques

1. **Task 1: Data Ingestion Pipeline**

   - **Script:** `Task1_Data_Ingestion_Pipeline.py`
   - **Description:** Sets up a data ingestion pipeline to load customer transaction data from various sources into HDFS, ensuring fault tolerance and data integrity.
   - **Run Command:**

     ```bash
     python PartB/Task1_Data_Ingestion_Pipeline.py
     ```

2. **Task 2: Data Storage and Querying Solution**

   - **Script:** `Task2_Data_Storage_and_Querying.py`
   - **Description:** Implements a data storage and querying solution using MongoDB.
   - **Run Command:**

     ```bash
     python PartB/Task2_Data_Storage_and_Querying.py
     ```

3. **Task 3: Real-Time Data Clustering System**

   - **Script:** `Task3_Real_Time_Data_Clustering.py`
   - **Description:** Builds a real-time data clustering system using Apache Spark to analyze data streams from social media platforms.
   - **Run Command:**

     ```bash
     python PartB/Task3_Real_Time_Data_Clustering.py
     ```

4. **Task 4: Data Streaming Pipeline with Kafka**

   - **Script:** `Task4_Data_Streaming_Pipeline.py`
   - **Description:** Sets up a data streaming pipeline with Kafka to integrate data for real-time analysis, ensuring data consistency and fault tolerance.
   - **Run Command:**

     ```bash
     python PartB/Task4_Data_Streaming_Pipeline.py
     ```

## Project Outcomes

- Successful integration and cleansing of healthcare datasets.
- Implementation of real-time data processing and clustering using Spark and Kafka.
- Storage and querying of data using MongoDB, ensuring scalability and flexibility.
- Robust data ingestion pipeline ensuring fault tolerance and data integrity.