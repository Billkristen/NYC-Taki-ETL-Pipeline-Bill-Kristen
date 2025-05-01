# NYC Taxi Data Engineering Project by Bill Kristen Indupalli

## Overview
This real-world ETL project ingests and processes public NYC Yellow Taxi trip data. Designed for production-style data engineering, it reflects the toolset and skills listed on my resume.

## Tech Stack
- **Python & SQL** – Core ETL processing
- **Apache Spark** – (optional for scalable transformation)
- **Apache Airflow** – (pluggable for orchestration and DAG scheduling)
- **AWS (S3)** – Public dataset hosting
- **Snowflake/Redshift** – Extendable target warehouse
- **Tableau / Power BI** – Data visualization & KPIs
- **Data Lakes** – Structured data zone simulated locally
- **Data Modeling** – Structured dimensional schema
- **Data Quality Checks** – Filtering & validations built-in
- **Service Level Agreements (SLA)** – Simulated 6AM daily delivery

## Use Cases
- Trip duration insights
- Fare trends by zone
- Peak travel periods
- Anomaly detection for fraud (future)

## Folder Structure
```
nyc-taxi-etl/
├── data/
├── etl/
├── warehouse/
├── analysis/
├── run_etl.py
├── requirements.txt
└── README.md
```

## Execution
```bash
pip install -r requirements.txt
python run_etl.py
```

## Author
**Bill Kristen Indupalli**  
4 years of experience (2Y Analyst, 2Y Engineer)  
Tools: Spark, Airflow, AWS, Tableau, SQL  
LinkedIn: www.linkedin.com/in/bill-kristen-indupalli  
