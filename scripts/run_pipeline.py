"""
Script Name: run_pipeline.py
Description: Master orchestration script that executes the complete 
             end-to-end data pipeline (API Ingestion -> Data Cleaning & Transformation).
Author: Data Analyst Mentor & Mentee
"""

import logging
import os
import subprocess
import sys

# Configure logging for pipeline orchestration monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


def run_script(script_path: str):
  """Executes a target Python script as a subprocess and checks for success."""
  logging.info(f"Starting execution of: {script_path}")

  try:
    # Run the script using the current Python interpreter
    result = subprocess.run(
        [sys.executable, script_path],
        check=True,
        text=True,
        capture_output=True,
    )
    logging.info(f"Successfully completed: {script_path}")
    if result.stdout:
      print(result.stdout)

  except subprocess.CalledProcessError as e:
    logging.error(f"Error occurred while executing {script_path}")
    logging.error(e.stderr)
    sys.exit(1)


def main():
  """Orchestrates the full end-to-end data pipeline."""
  logging.info("==============================================")
  logging.info("Starting Master World Bank Data Pipeline")
  logging.info("==============================================")

  scripts_dir = os.path.dirname(os.path.abspath(__file__))

  # Step 1: Run API Data Ingestion Script
  fetch_script = os.path.join(scripts_dir, "fetch_api.py")
  run_script(fetch_script)

  # Step 2: Run Data Cleaning and Transformation Script
  clean_script = os.path.join(scripts_dir, "clean_data.py")
  run_script(clean_script)

  logging.info("==============================================")
  logging.info("Master Pipeline Completed Successfully!")
  logging.info("==============================================")


if __name__ == "__main__":
  main()