import boto3

# AWS S3 configuration
s3 = boto3.client(
    's3',
    aws_access_key_id='ASIAVOPPYZVWFZELNMVK',
    aws_secret_access_key='jcrRWWsEMds+bl53ZTnUWAFl2LgvFxuHZkH+ArWo'
)

bucket_name = 'roipredictionproject'
file_name = 'DE_ROI_dataset1.csv'
local_file = "C://Users//harsha k g//Downloads//DE_ROI_dataset.csv"

# Upload local file to S3
s3.upload_file(local_file, bucket_name, file_name)
print(f"File {file_name} uploaded to bucket {bucket_name}")

from pyspark.sql import SparkSession

# Start Spark session
spark = SparkSession.builder \
    .appName("Data Cleaning") \
    .getOrCreate()

# Load data from S3
data = spark.read.csv("s3://roipredictionproject/DE_ROI_data/DE_ROI_dataset.csv", header=True)

# Perform cleaning operations
cleaned_data = data.dropna()

# Save cleaned data back to S3
cleaned_data.write.csv("s3://roipredictionproject/DE_ROI_data/Cleaned_DE_ROI_dataset.csv", header=True)
print("Data cleaning completed and saved to S3.")
