"""
Script Name: clean_data.py
Description: Reads raw JSON files, flattens nested structures, handles missing values,
             merges multiple indicators into a master dataset, and exports to CSV.
Author: Data Analyst Mentor & Mentee
"""

import glob
import logging
import os
import sys
import pandas as pd

# Configure logging for pipeline monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


class DataCleaner:
  """Handles data cleaning, flattening, transformation, and merging for World Bank datasets."""

  def __init__(self, raw_dir: str, processed_dir: str):
    self.raw_dir = raw_dir
    self.processed_dir = processed_dir

    # Ensure processed data directory exists
    os.makedirs(self.processed_dir, exist_ok=True)

  def flatten_json_to_dataframe(self, file_path: str) -> pd.DataFrame:
    """Reads a raw JSON file and flattens it into a Pandas DataFrame."""
    try:
      df = pd.read_json(file_path)

      if df.empty:
        logging.warning(f"File {file_path} is empty.")
        return pd.DataFrame()

      # Extract relevant nested fields if present
      # World Bank JSON structure places country and indicator inside nested dictionaries
      records = []
      # Re-read raw file using standard json module to safely parse nested structures
      import json

      with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

      for item in data:
        country_info = item.get("country", {})
        indicator_info = item.get("indicator", {})

        record = {
            "country_code": country_info.get("id"),
            "country_name": country_info.get("value"),
            "indicator_code": indicator_info.get("id"),
            "indicator_name": indicator_info.get("value"),
            "year": item.get("date"),
            "value": item.get("value"),
        }
        records.append(record)

      flat_df = pd.DataFrame(records)
      return flat_df

    except Exception as e:
      logging.error(f"Error processing {file_path}: {e}")
      return pd.DataFrame()

  def process_all_files(self) -> pd.DataFrame:
    """Iterates through all raw JSON files, flattens them, and combines into a master DataFrame."""
    search_pattern = os.path.join(self.raw_dir, "*.json")
    json_files = glob.glob(search_pattern)

    if not json_files:
      logging.error(f"No raw JSON files found in {self.raw_dir}")
      return pd.DataFrame()

    all_dfs = []
    for file_path in json_files:
      logging.info(f"Flattening file: {file_path}")
      df = self.flatten_json_to_dataframe(file_path)
      if not df.empty:
        all_dfs.append(df)

    if not all_dfs:
      logging.error("No valid dataframes generated from raw JSON files.")
      return pd.DataFrame()

    master_df = pd.concat(all_dfs, ignore_index=True)
    return master_df

  def transform_and_pivot(self, master_df: pd.DataFrame) -> pd.DataFrame:
    """Pivots indicator rows into individual columns, handles data types and missing values."""
    logging.info("Transforming and pivoting master dataset...")

    # Ensure year is numeric integer
    master_df["year"] = pd.to_numeric(master_df["year"], errors="coerce")

    # Filter out records with null years or country codes
    master_df = master_df.dropna(subset=["country_code", "year", "indicator_name"])

    # Pivot table so each indicator becomes its own column
    pivoted_df = master_df.pivot_table(
        index=["country_code", "country_name", "year"],
        columns="indicator_name",
        values="value",
    ).reset_index()

    # Clean up column names (replace spaces with underscores, lowercase)
    pivoted_df.columns.name = None  # Remove pivot index name

    # Sort values by country and year for clean time-series ordering
    pivoted_df = pivoted_df.sort_values(
        by=["country_name", "year"]
    ).reset_index(drop=True)

    return pivoted_df

  def run_cleaning_pipeline(self):
    """Executes the complete data cleaning and transformation workflow."""
    logging.info("Starting Data Cleaning Pipeline...")

    master_df = self.process_all_files()
    if master_df.empty:
      logging.error("Pipeline aborted due to empty master dataset.")
      return

    transformed_df = self.transform_and_pivot(master_df)

    # Save processed master dataset to CSV
    output_file = os.path.join(self.processed_dir, "master_economic_data.csv")
    transformed_df.to_csv(output_file, index=False)
    logging.info(f"Successfully saved cleaned master dataset to {output_file}")


if __name__ == "__main__":
  RAW_DIR = os.path.join("data", "raw")
  PROCESSED_DIR = os.path.join("data", "processed")

  cleaner = DataCleaner(raw_dir=RAW_DIR, processed_dir=PROCESSED_DIR)
  cleaner.run_cleaning_pipeline()