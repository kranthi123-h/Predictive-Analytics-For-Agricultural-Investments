CREATE EXTERNAL TABLE roi_prediction_table2 (
  Season STRING,
  Domain STRING,
  Area_Code STRING,
  Area STRING,
  Element STRING,
  Item_Code STRING,
  Item STRING,
  Year INT,
  Total_Cost FLOAT,
  Avg_temp FLOAT,
  average_rain_fall_mm_per_year FLOAT,
  Feature_2 FLOAT,
  Quantity_of_the_pesticides FLOAT,
  ROI FLOAT,
  Total_Cost_ROI_percent FLOAT
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
LOCATION 's3://roipredictionproject/DE_ROI_data/';
