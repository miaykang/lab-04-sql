import logging
import os
import sys
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt


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


def get_db_connection():
   """Establishes and returns a connection to the MySQL database."""
   try:
       connection = mysql.connector.connect(
           host=DB_HOST,
           user=DB_USER,
           password=DB_PASSWORD,
           database=DB_NAME,
           port=int(DB_PORT),
       )
       return connection
   except mysql.connector.Error as err:
       logging.error(f"Failed to connect to '{DB_NAME}': {err}")
       raise


def get_data_by_group(value: str) -> pd.DataFrame:
   """Retrieves all rows from the 'mock' table where the 'group' column equals the given value.
   Returns: DataFrame containing matching rows from the database.
   """
   logging.info(f"Querying table 'mock' where `group` = '{value}'...")
   query = "SELECT * FROM `mock` WHERE `group` = %s;"


   connection = None
   try:
       connection = get_db_connection()
       df = pd.read_sql_query(query, connection, params=(value,))
       logging.info(f"Query returned {len(df)} rows for `group` = '{value}'.")
       return df
   except Exception as err:
       logging.error(f"Error executing get_data_by_group for value '{value}': {err}")
       raise
   finally:
       if connection and connection.is_connected():
           connection.close()




def plot_counts(groupby: str) -> pd.DataFrame:
   """Queries row counts grouped by a specified column and displays a bar plot.
   Returns aggregated DataFrame containing column values and their row counts.
   """
   logging.info(f"Fetching record counts grouped by column '{groupby}'...")
   query = f"""
   SELECT `{groupby}`, COUNT(*) AS record_count
   FROM `mock`
   GROUP BY `{groupby}`
   ORDER BY record_count DESC;
   """
   connection = None
   try:
       connection = get_db_connection()
       counts_df = pd.read_sql_query(query, connection)
       logging.info(f"Successfully retrieved group counts for '{groupby}'.")
       if not counts_df.empty:
           plt.bar(counts_df[groupby].astype(str), counts_df["record_count"])
           plt.tight_layout()
           plt.show()
       return counts_df


   except Exception as err:
       logging.error(f"Error executing plot_counts for column '{groupby}': {err}")
       raise
   finally:
       if connection and connection.is_connected():
           connection.close()


def main():
   """Execution function"""
   print("\n--- shows get_data_by_group() ---")
   group_value = "Alpha"
   group_data = get_data_by_group(group_value)
   print(f"\nFirst 5 rows for group '{group_value}':")
   print(group_data.head())


   print("\n---  plot_counts() ---")
   counts = plot_counts(groupby="group")
   print("\nGroup Count Summary:")
   print(counts)

if __name__ == "__main__":
   main()