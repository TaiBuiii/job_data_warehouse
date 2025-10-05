# 🧠 Job Data Warehouse

## 1️⃣ Overview
This project implements a **Medallion Data Warehouse architecture** (Bronze → Silver → Gold) to build an automated data pipeline.

Data is **crawled from TopCV**, stored in **PostgreSQL**, and orchestrated by **Apache Airflow**.  
The purpose is to analyze job trends — including the most demanded **skills**, **programming languages**, and **positions** in the market.

---

### ⚙️ Tech Stack

| Component | Description |
|------------|-------------|
| **Apache Airflow** | Orchestrates and schedules the ETL/ELT pipeline |
| **PostgreSQL** | Stores data in bronze, silver, and gold schemas |
| **Python** | Extracts, cleans, and transforms job data |
| **Docker Compose** | Sets up the entire environment easily |

---

## 2️⃣ How to Run

1. **Initialize Airflow environment**
```bash
   docker compose up airflow-init
   docker compose up -d
```
2. **Folder structure**
```bash
├── config/
│   └── airflow.cfg                     # Airflow config file
├── logs/                               # Task logs
├── plugins/                            # Airflow plugins (if any)
├── dags/
│   ├── ELT.py                          # Main DAG pipeline
│   ├── logger.py                       # Logging setup
│   ├── mapping.py                      # Helper mapping script
│   ├── extract/
│   │   └── extract.py                  # Crawl job data from TopCV
│   ├── transform/
│   │   └── transform.py                # Data cleaning and standardization
│   └── load/
│       ├── load_bronze.py              # Load raw data into bronze schema
│       ├── load_silver.py              # Process and load silver data
│       └── load_gold.py                # Build final fact & dimension tables
├── sql/
│   ├── init_database.sql               # Initialize DB schemas and tables
│   ├── dim_*.sql                       # Dimension tables (location, skill, etc.)
│   ├── fact_*.sql                      # Fact tables
│   └── bridge_*.sql                    # Bridge (many-to-many) tables
├── docker-compose.yaml                 # Docker environment setup
├── .env                                # Environment variables (Postgres, Airflow)
└── README.md
