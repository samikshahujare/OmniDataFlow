# OmniDataFlow
> End-to-End API Integration Engine, Automated Python ETL & Power BI Executive Reporting Suite

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![ETL Pipeline](https://img.shields.io/badge/ETL-Automated_Pipeline-orange.svg)]()
[![Power BI](https://img.shields.io/badge/Power_BI-Executive_Dashboard-yellow.svg)]()
[![REST API](https://img.shields.io/badge/API-World_Bank_REST-green.svg)]()

An end-to-end **Data Engineering and Business Intelligence** project that extracts live global socioeconomic data from the **World Bank REST API**, transforms nested JSON into analytics-ready datasets using Python, performs feature engineering, and delivers an interactive multi-page **Power BI Executive Dashboard** for data-driven decision making.

---

# 📌 Project Highlights

- Built an automated ETL pipeline using Python and REST APIs.
- Processed and flattened nested JSON responses into structured datasets.
- Engineered GDP per Capita and GDP Growth analytical features.
- Designed an interactive Power BI dashboard with multiple report pages.
- Implemented DAX measures, KPI cards, maps, trend analysis, and data quality monitoring.
- Created reusable, scalable workflows for future API integrations.

---

# 🏗️ Solution Architecture

```text
                     World Bank REST API
                             │
                  HTTP GET Requests (requests)
                             │
                             ▼
                   Raw JSON Data Collection
                             │
                             ▼
         Python ETL Pipeline (Pandas + NumPy)
    Cleaning • Flattening • Validation • Transformation
                             │
                             ▼
             Processed & Historical CSV Files
                             │
                             ▼
          Power Query Data Transformation
                             │
                             ▼
               Power BI Data Modeling (DAX)
                             │
                             ▼
           Interactive Executive Dashboard
```

---

# 🚀 Key Features

### 🔹 Automated API Data Ingestion

- Extracts live socioeconomic indicators using the World Bank REST API.
- Supports API pagination for large datasets.
- Stores raw JSON responses for reproducibility.
- Creates structured historical datasets.

---

### 🔹 Data Cleaning & Transformation

- Parses nested JSON objects.
- Handles missing values.
- Standardizes column names and data types.
- Removes duplicate records.
- Generates analytics-ready tabular datasets.

---

### 🔹 Feature Engineering

Derived business metrics include:

- GDP per Capita
- GDP Annual Growth Rate
- Inflation Rate
- Population Trends
- Historical Economic Indicators

---

### 🔹 Interactive Power BI Dashboard

Includes:

- Executive Dashboard
- Country Analysis
- Trend Analysis
- Data Quality Dashboard

---

# 📊 Dashboard Preview

## 🌍 Executive Dashboard

Provides a high-level overview of global economic performance with KPI cards, interactive filters, GDP trends, and country comparisons.

![Executive Dashboard](images/Executive%20Dashboard.png)

---

## 🌎 Country Analysis

Analyze country-level economic indicators using interactive tables and geographic visualizations.

![Country Analysis](images/Country%20Analysis.png)

---

## 📈 Trend Analysis

Visualize historical GDP growth, inflation trends, and relationships between key economic indicators.

![Trend Analysis](images/Trend%20Analysis.png)

---

## ✅ Data Quality Dashboard

Monitor dataset quality through record counts, missing values, refresh timestamps, and pipeline validation metrics.

![Data Quality Dashboard](images/Data%20Quality%20Dashboard.png)

---

# 📈 Dashboard Capabilities

### Executive Dashboard

- Total GDP
- Average GDP per Capita
- Average Inflation Rate
- Average GDP Growth
- Interactive KPI Cards
- GDP Trend Analysis

### Country Analysis

- Country-wise Economic Indicators
- Interactive Geographic Map
- GDP Comparison
- Population Analysis

### Trend Analysis

- GDP Growth vs Inflation
- GDP per Capita vs Life Expectancy
- Historical Trend Visualization

### Data Quality Dashboard

- Total Record Count
- Missing Value Analysis
- Data Validation Metrics
- Refresh Timestamp Monitoring

---

# 🛠 Technology Stack

## Programming

- Python
- Pandas
- NumPy
- Requests

## Data Engineering

- REST API
- JSON
- CSV
- ETL Pipeline

## Business Intelligence

- Power BI
- Power Query
- DAX

## Development Tools

- Visual Studio Code
- Git
- GitHub
- Jupyter Notebook

---

# 📂 Project Structure

```text
RealTime_API_Dashboard/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── historical/
│
├── images/
│   ├── executive_dashboard.png
│   ├── country_analysis.png
│   ├── trend_analysis.png
│   └── data_quality_dashboard.png
│
├── notebooks/
│   ├── 01_API_Testing.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   └── 03_Data_Analysis.ipynb
│
├── scripts/
│   ├── fetch_api.py
│   ├── clean_data.py
│   └── run_pipeline.py
│
├── powerbi/
│   └── RealTimeDashboard.pbix
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

# 🌐 Dataset Source

**World Bank Open Data API**

https://api.worldbank.org/

Economic indicators include:

- GDP
- GDP Growth
- GDP per Capita
- Inflation
- Population
- Life Expectancy
- Unemployment

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/samikshahujare/RealTime_API_Dashboard.git
```

```bash
cd RealTime_API_Dashboard
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execute Complete ETL Pipeline

```bash
python scripts/run_pipeline.py
```

---

## Launch Power BI Dashboard

Open

```text
powerbi/RealTimeDashboard.pbix
```

using **Power BI Desktop**.

---

# 📚 Python Libraries

| Library | Purpose |
|----------|----------|
| Requests | REST API Integration |
| Pandas | Data Cleaning & Transformation |
| NumPy | Numerical Computing |
| JSON | API Response Parsing |

---

# 📊 Power BI Skills Demonstrated

- Power Query
- Data Modeling
- DAX Measures
- KPI Cards
- Interactive Slicers
- Maps
- Scatter Charts
- Line Charts
- Bar Charts
- Executive Dashboards
- Data Quality Monitoring

---

# 💼 Data Engineering Skills Demonstrated

- REST API Integration
- ETL Pipeline Development
- Data Cleaning
- Feature Engineering
- Historical Data Storage
- JSON Processing
- Data Validation
- Automated Data Workflows

---

# 🎯 Business Value

This solution demonstrates how live API data can be transformed into reliable business intelligence through automated ETL pipelines and interactive dashboards, enabling data-driven decision-making using real-time socioeconomic indicators.

---

# 🔮 Future Enhancements

- SQL Database Integration
- Incremental Data Loading
- Azure Data Factory Pipeline
- Scheduled Power BI Refresh
- Docker Containerization
- CI/CD Deployment using GitHub Actions
- Cloud Data Warehouse Integration

---

# 👩‍💻 Author

**Samiksha Hujare**

**GitHub**

https://github.com/samikshahujare

**LinkedIn**

https://www.linkedin.com/in/samiksha-hujare

---

## ⭐ If you found this project helpful, consider giving it a star!
