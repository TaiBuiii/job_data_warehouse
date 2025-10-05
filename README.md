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
│     └── airflow.cfg
├── logs/
├── plugins/
├── dags/
│     ├── ELT.py
│     ├── logger.py
│     ├── mapping.py
│     ├── extract/
│     │   └── extract.py
│     ├── transform/
│     │   └── transform.py
│     └── load/
│         ├── load_bronze.py         
│         ├── load_silver.py        
│         └── load_gold.py           
├── sql/
│     ├── init_database.sql
│     ├── dim_company.sql        
│     ├── fact_recruitment.sql
│     ├── dim_location.sql
│     ├── dim_skill.sql
│     ├── dim_programming_language.sql 
│     ├── dim_job.sql
│     ├── dim_position.sql
│     ├── dim_education.sql
│     ├── bridge_job_location.sql
│     ├── bridge_job_programming_language.sql
│     └── bridge_job_skill.sql
├── docker-compose.yaml
├── .env                       
└── README.md
```
