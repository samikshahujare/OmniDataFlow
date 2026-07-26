"""
Script Name: fetch_api.py
Description: Automates the extraction of live multi-indicator datasets 
             from the World Bank REST API for multiple countries and saves raw JSON payloads.
Author: Data Analyst Mentor & Mentee
"""

import json
import logging
import os
import sys
import requests

# Configure logging for production monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


class WorldBankAPICollector:
  """Handles automated extraction and raw storage of World Bank REST API data."""

  def __init__(self, countries: list, indicators: dict, raw_data_dir: str):
    self.countries = countries
    self.indicators = indicators
    self.raw_data_dir = raw_data_dir
    self.base_url = "http://api.worldbank.org/v2"

    # Ensure raw data directory exists
    os.makedirs(self.raw_data_dir, exist_ok=True)

  def fetch_indicator_data(self, country_code: str, indicator_code: str) -> list:
    """Fetches all pages of data for a specific country and indicator."""
    all_records = []
    page = 1
    max_pages = 1  # Will be updated dynamically from API metadata

    while page <= max_pages:
      url = (
          f"{self.base_url}/country/{country_code}/indicator/{indicator_code}"
          f"?format=json&per_page=100&page={page}"
      )

      try:
        logging.info(f"Fetching {country_code} - {indicator_code} (Page {page})")
        response = requests.get(url, timeout=15)

        if response.status_code == 200:
          payload = response.json()

          # Validate response structure
          if isinstance(payload, list) and len(payload) == 2:
            metadata = payload[0]
            records = payload[1]

            max_pages = metadata.get("pages", 1)

            if records:
              all_records.extend(records)

            page += 1
          else:
            logging.error(
                f"Unexpected payload format for {country_code} - {indicator_code}"
            )
            break
        else:
          logging.warning(
              f"API returned status code {response.status_code} for {url}"
          )
          break

      except requests.exceptions.RequestException as e:
        logging.error(f"Network error during request to {url}: {e}")
        break

    return all_records

  def run_pipeline(self):
    """Executes the complete ingestion pipeline across all configured countries and indicators."""
    logging.info("Starting World Bank API Data Ingestion Pipeline...")

    for country in self.countries:
      for ind_name, ind_code in self.indicators.items():
        logging.info(f"Processing Indicator: {ind_name} ({ind_code}) for Country: {country}")

        data = self.fetch_indicator_data(country, ind_code)

        if data:
          file_name = f"{country}_{ind_name.replace(' ', '_').lower()}.json"
          file_path = os.path.join(self.raw_data_dir, file_name)

          try:
            with open(file_path, "w", encoding="utf-8") as f:
              json.dump(data, f, indent=4)
            logging.info(f"Successfully saved raw data to {file_path}")
          except IOError as e:
            logging.error(f"Failed to write raw data file {file_path}: {e}")
        else:
          logging.warning(f"No records retrieved for {country} - {ind_name}")

    logging.info("Data Ingestion Pipeline completed successfully.")


if __name__ == "__main__":
  # Define target countries (ISO 3-letter codes)
  TARGET_COUNTRIES = ["IND", "USA", "CHN", "DEU", "BRA"]

  # Define target economic and social indicators with World Bank indicator codes
  TARGET_INDICATORS = {
      "GDP": "NY.GDP.MKTP.CD",
      "Population": "SP.POP.TOTL",
      "Inflation": "FP.CPI.TOTL.ZG",
      "Unemployment": "SL.UEM.TOTL.ZS",
      "CO2_Emissions": "EN.ATM.CO2E.KT",
      "Life_Expectancy": "SP.DYN.LE00.IN",
  }

  RAW_DIR = os.path.join("data", "raw")

  # Instantiate collector and run ingestion pipeline
  collector = WorldBankAPICollector(
      countries=TARGET_COUNTRIES,
      indicators=TARGET_INDICATORS,
      raw_data_dir=RAW_DIR,
  )
  collector.run_pipeline()