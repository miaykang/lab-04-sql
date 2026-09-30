import logging
import pandas as pd
import os
import sys
import mysql.connector
from sqlalchemy import create_engine


logging.basicConfig(
   level=logging.INFO,
   format="%(asctime)s [%(levelname)s] %(message)s",
   handlers=[logging.StreamHandler(sys.stdout)],
)


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "ds2022")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_PORT = os.getenv("DB_PORT", "3306")


def read_data(filename):
   """Loads data from a CSV file into a pandas dataframe"""
   df = pd.read_csv(filename)
   return df


def clean_data(data):
   """Cleans the data by dropping any rows with missing values"""
   data = data.dropna()
   return data


def load_data(data, table='mock'):
   """Loads data from a pandas dataframe into a MySQL database"""
   connection_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
   logging.info(f"Connecting to database: {connection_url}")


   try:
       engine = create_engine(connection_url)
       with engine.connect() as connection:
           data.to_sql(table, connection, if_exists='replace', index=False)
       logging.info(f"Data loaded successfully into table: {table}")
   except Exception as e:
       logging.error(f"Error loading data: {e}")
       raise


def main():
   """Main function to run the pipeline"""
   csv_file_path = "MOCK_DATA.csv"


   logging.info("Starting Pipeline")
   raw_df = read_data(csv_file_path)
   cleaned_df = clean_data(raw_df)


   load_data(data=cleaned_df, table="mock")
   logging.info("Pipeline Completed Successfully")


if __name__ == "__main__":
   main()
