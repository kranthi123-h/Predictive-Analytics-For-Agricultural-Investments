

# ROI Prediction Project

This project aims to predict the Return on Investment (ROI) for various crops based on user-selected parameters such as temperature, rainfall, pesticide quantity, total cost, and country-specific base values. The data pipeline is built using AWS services for data storage, processing, and analysis, and integrates with Power BI for visualization.

---

## Project Architecture

### Workflow Overview

1. **Data Sources**:
   - Multiple datasets from different sources are consolidated into a single database.
   
2. **Data Storage**:
   - Data is extracted and stored in an **AWS S3** bucket using **Boto3**, AWS's Python SDK.

3. **Data Processing**:
   - Raw data is cleaned and processed using **AWS EMR** (Elastic MapReduce) with Apache Spark.

4. **Storage of Cleaned Data**:
   - Processed data is saved back into the S3 bucket.

5. **Querying Data**:
   - **Amazon Athena** is used to run SQL-like queries directly on the cleaned data stored in S3.

6. **Data Integration**:
   - Results from Athena queries are connected to Power BI using the **Amazon Athena ODBC driver**.

7. **Data Analysis**:
   - **Power BI** is used for data visualization and analysis using DAX (Data Analysis Expressions).

---

## Key AWS Services Used

1. **AWS S3**:
   - Central storage for raw and cleaned datasets.

2. **AWS EMR**:
   - Processes large datasets using Apache Spark for data cleaning and transformation.

3. **Amazon Athena**:
   - SQL-based querying engine to analyze data stored in S3.

4. **Boto3**:
   - Python library for interaction with AWS services (used for S3 operations).

---

## Implementation Steps

### Data Upload
- Data is uploaded to the S3 bucket using **Boto3**.
- Example script for uploading a file:
  ```python
  import boto3
  
  s3 = boto3.client(
      's3',
      aws_access_key_id='YOUR_AWS_ACCESS_KEY',
      aws_secret_access_key='YOUR_AWS_SECRET_KEY'
  )
  
  bucket_name = 'your-s3-bucket-name'
  file_name = 'your-file.csv'
  s3.upload_file(file_name, bucket_name, file_name)
  ```

### Data Cleaning and Processing
- Use **AWS EMR** to process raw data:
  - Launch a cluster with **Apache Spark**.
  - Clean the data using PySpark.
  - Save cleaned data back to S3.

### Querying Data with Athena
- Create a table in Athena pointing to the cleaned data in S3.
- Run SQL queries to fetch data:
  ```sql
  SELECT * FROM your_table WHERE country = 'USA';
  ```

### Visualization with Power BI
- Connect to Amazon Athena using the ODBC driver.
- Visualize the data and build interactive dashboards using DAX expressions.

---

## Example ROI Calculation Formula
The ROI is calculated using the following formula:

```
Predicted ROI = 
    (0.1 * Rainfall) +
    (0.2 * Pesticide Quantity) +
    (0.3 * Total Cost) +
    (0.25 * Temperature) +
    SWITCH(Country, "USA", 50, "India", 70, 0)
```

The user can interactively:
1. Select the **country** (e.g., USA, India).
2. Choose **crop type** and **season**.
3. Adjust parameters using sliders in Power BI to get a personalized ROI prediction.

---

## Folder Structure
```
ROI_Prediction_Project/
│
├── data/
│   ├── raw_data.csv            # Original datasets
│   ├── cleaned_data.csv        # Processed datasets
│
├── scripts/
│   ├── upload_to_s3.py         # Script to upload data to S3
│   ├── process_data_emr.py     # Script to process data on EMR
│
├── notebooks/
│   ├── analysis.ipynb          # Jupyter Notebook for analysis
│
├── assets/
│   ├── architecture_diagram.png # Workflow diagram
│
├── README.md                   # Project overview
└── requirements.txt            # Python dependencies
```

---

## Requirements

- Python 3.x
- Boto3
- AWS CLI
- Power BI
- Apache Spark (via AWS EMR)

---

## Setup and Usage

### Step 1: Upload Data to S3
- Run `upload_to_s3.py` to upload raw data to S3.

### Step 2: Process Data with EMR
- Create and start an EMR cluster with Spark.
- Use `process_data_emr.py` to clean and process the data.

### Step 3: Query Data with Athena
- Configure Athena to query the cleaned data stored in S3.

### Step 4: Visualize Data in Power BI
- Connect Athena to Power BI via the ODBC driver and build interactive dashboards.

---

