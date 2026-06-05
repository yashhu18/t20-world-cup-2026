# T20 World Cup Analytics Platform

## Overview

The T20 World Cup Analytics Platform is an end-to-end data engineering project designed to collect, process, transform, and analyze international cricket data. The platform leverages modern data engineering practices to build scalable data pipelines, analytics-ready datasets, and interactive dashboards for player, team, and tournament performance analysis.

This project demonstrates expertise in cloud-based data engineering, ETL/ELT development, data modeling, orchestration, and analytics.

---

## Business Problem

Cricket generates large volumes of match, player, and tournament data. Analysts, coaches, and fans often require consolidated insights across multiple seasons and tournaments.

The goal of this project is to:

- Centralize cricket datasets from multiple sources
- Build reliable ETL pipelines
- Transform raw data into analytics-ready models
- Generate meaningful insights through dashboards
- Enable advanced analytics and future predictive modeling

---

## Solution Architecture

Source Data → Data Ingestion → Data Lake → Data Transformation → Data Warehouse → Reporting Layer

### Data Flow

1. Extract match, player, and tournament data from source files and APIs.
2. Load raw datasets into the data lake.
3. Transform data using PySpark and SQL.
4. Apply data quality checks and validation.
5. Create curated datasets using Medallion Architecture.
6. Load transformed data into analytical tables.
7. Build dashboards and performance reports.

---

## Technologies Used

### Programming

- Python
- SQL
- PySpark

### Data Engineering

- Apache Spark
- Delta Lake
- Apache Airflow
- Databricks

### Cloud & Storage

- Azure Data Lake Storage
- Azure Data Factory
- Azure Databricks

### Analytics

- Power BI
- Tableau

### DevOps

- Git
- GitHub Actions

---

## Data Model

The platform follows a dimensional modeling approach.

### Fact Tables

- Fact_Matches
- Fact_Batting_Statistics
- Fact_Bowling_Statistics
- Fact_Player_Performance

### Dimension Tables

- Dim_Player
- Dim_Team
- Dim_Venue
- Dim_Tournament
- Dim_Date

---

## Key Features

### Data Ingestion

- Automated ingestion of cricket datasets
- Incremental data loading
- Source validation and error handling

### Data Transformation

- Data cleansing and standardization
- Schema validation
- Aggregation and enrichment

### Analytics

- Team performance analysis
- Player performance analysis
- Tournament statistics
- Historical trend analysis
- Venue-based insights

### Data Quality

- Null value checks
- Duplicate record detection
- Data completeness validation
- Automated pipeline monitoring

---

## Dashboard Insights

The dashboard provides:

### Team Analytics

- Win percentage
- Run rate analysis
- Team comparison metrics

### Player Analytics

- Top run scorers
- Highest wicket takers
- Strike rate analysis
- Economy rate analysis

### Tournament Analytics

- Match outcomes
- Venue statistics
- Season trends
- Performance comparisons

---

## Project Structure

```text
t20-world-cup-2026
│
├── data
│   ├── raw
│   ├── processed
│   └── curated
│
├── notebooks
│
├── pipelines
│
├── sql
│
├── dashboards
│
├── docs
│
└── README.md
```

---

## Future Enhancements

- Real-time streaming with Apache Kafka
- Live match analytics
- Machine Learning-based match prediction
- GenAI-powered cricket analytics assistant
- Automated data lineage and governance framework

---

## Skills Demonstrated

- Data Engineering
- ETL/ELT Development
- Data Modeling
- Data Warehousing
- Apache Spark
- PySpark
- Databricks
- Azure Data Factory
- Delta Lake
- Data Quality Frameworks
- Power BI
- Cloud Data Platforms
- Analytics Engineering

---

## Author

### Yashwanth Vurukala

Data Engineer

**Tech Stack:** Azure | AWS | Databricks | PySpark | SQL | Microsoft Fabric | Airflow | Kafka

LinkedIn: www.linkedin.com/in/yashwanth-vurukala

GitHub: github.com/yashhu18

Email: yashwanth2022v@gmail.com
