# Containerized Kaggle-to-Postgres ETL Pipeline

This project demonstrates a professional-grade ETL (Extract, Transform, Load) pipeline containerized with **Docker**. It automates the process of fetching real-world weather datasets from Kaggle, performing data cleaning, and ingesting them into a structured PostgreSQL database.

---

## System Architecture

The system is orchestrated using **Docker Compose**, managing three primary services:
1. **ETL Worker (Python):** Handles API authentication, data extraction, and transformation using Pandas and SQLAlchemy.
2. **Database (PostgreSQL 15):** A robust relational database for persistent data storage.
3. **Management UI (pgAdmin 4):** A web-based interface for database monitoring and SQL querying.



---

##  Technical Features

* **Layered Containerization:** Optimized `Dockerfile` using `python:3.11-slim` to minimize image size and improve deployment speed.
* **Automated Data Transformation:** - Standardizes column headers (lowercase, underscores) for SQL compatibility.
  - Implements data lineage by adding `ingested_at` timestamps to every record.
  - Handles missing values using vectorized Pandas operations.
* **Robust Service Orchestration:** - Utilizes Docker **Healthchecks** to ensure the database is ready before the ETL worker starts.
  - Secured credential management via local **Volume Mounting** of Kaggle API keys.
* **Database Management:** Pre-configured pgAdmin environment for immediate data verification.

---

## Comparison: Manual vs. Automated ETL

| Feature | Manual Process | This Containerized Pipeline |
| :--- | :--- | :--- |
| **Setup Time** | High (Configuring local DB/Python) | Low (`docker-compose up`) |
| **Consistency** | Low (Dependency conflicts) | High (Identical environment for all users) |
| **Reliability** | Manual error-prone steps | Automated healthchecks & error handling |
| **Security** | Hardcoded credentials | Secured volume mounting |

---

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Kaggle API key (`kaggle.json`) at `~/.kaggle/`

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
2. **Start the pipeline:**
   docker-compose up --build
3. **Verify Data:**

- Open http://localhost:8085 (pgAdmin).

- Log in with admin@admin.com / root.

Check the kaggle_weather table in the openAQ database.


## Repository Structure
**Dockerfile**: Multi-layer Python environment configuration.

**docker-compose.yaml**: Service orchestration and dependency management.

**ingest.py**: Core ETL logic (Pandas/SQLAlchemy).

**requirements.txt**: Managed dependency list.

**.gitignore**: Pre-configured to exclude sensitive keys and database volumes.