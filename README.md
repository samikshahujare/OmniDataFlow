# Real-Time API Data Integration & Analytics Dashboard

An end-to-end Data Engineering and Analytics project that extracts live global socioeconomic datasets from the World Bank REST API, processes and flattens nested JSON payloads using Python, stores feature-engineered historical records, and powers an interactive multi-page Executive Dashboard in Power BI.

---

## 📊 Project Architecture

[World Bank REST API]
│ (HTTP GET / Requests)
▼
[data/raw/ (JSON Payloads)]
│ (Python Cleaning & Flattening / Pandas)
▼
[data/processed/ & data/historical/ (Master CSVs)]
│ (Power Query & DAX Modeling)
▼
[Power BI Executive Dashboard (.pbix)]

---

## 🚀 Key Features
• **Automated API Ingestion:** Python script utilizing the `requests` library with pagination handling to pull live multi-indicator datasets across global economies.<br>
• **Data Cleaning & Transformation:** Flattens nested JSON structures, standardizes data types, handles missing values, and pivots indicators into a clean wide-format tabular structure.<br>
• **Advanced Feature Engineering:** Computes GDP per Capita and Year-over-Year percentage growth rates using Pandas.<br>
• **End-to-End Orchestration:** Master pipeline script (`run_pipeline.py`) automating extraction and transformation workflows.<br>
• **Executive BI Reporting:** Multi-page Power BI dashboard featuring dynamic KPIs, trend lines, geographic maps, and advanced DAX measures.

---

## 🛠️ Tech Stack
* **Programming & ETL:** Python, Requests, Pandas, NumPy, Jupyter Notebook
* **API & Data Formats:** REST APIs, JSON, CSV
* **Data Visualization & BI:** Power BI, Power Query, DAX
* **Version Control:** Git, GitHub
* **Environment:** VS Code

---

## 📁 Project Structure
```text
RealTime_API_Dashboard/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── historical/
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
├── requirements.txt
└── README.md
