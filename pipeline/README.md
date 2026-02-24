# Containerized Kaggle-to-Postgres ETL Pipeline

This project demonstrates a ETL (Extract, Transform, Load) pipeline containerized with **Docker**. It fetches real-world weather datasets from Kaggle and ingest them into a structured PostgreSQL database.

---

## System Architecture

The system is orchestrated using **Docker Compose**, managing three primary services:
1. **ETL Worker (Python):** Handles API authentication, data extraction, and transformation using Pandas and SQLAlchemy.
2. **Database (PostgreSQL 15):** A robust database for persistent data storage.
3. **Management UI (pgAdmin 4):** A web-based interface for database monitoring and SQL querying.



---

##  Technical Features

* **Layered Containerization:** Optimized `Dockerfile` using `python:3.11-slim` to minimize image size and improve deployment speed.
* **Robust Service Orchestration:** - Utilizes Docker **Healthchecks** to ensure the database is ready before the ETL worker starts.
  - Secured credential management via local **Volume Mounting** of Kaggle API keys.
* **Database Management:** Pre-configured pgAdmin environment for immediate data verification.

---

## Getting Started

### Prerequisites
- Docker & Docker Compose( make sure Docker is up and running)
- Kaggle API key (`kaggle.json`) at `~/.kaggle/`

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone <repo-link>
2. **Start the pipeline:**
   docker-compose up --build
3. **Verify Data:**

- Open http://localhost:8085 (pgAdmin).

- Log in with admin@admin.com / root.
- After login in pgAdmin-
- Servers -> register -> server -> connection
  Hostname: pgdatabase
  Port: 5432
  Maintenance database: openAQ
  Username: admin
  password: root

Check the kaggle_weather table in the openAQ database.


## Repository Structure
**Dockerfile**: Multi-layer Python environment configuration.

**docker-compose.yaml**: Service orchestration and dependency management.

**ingest.py**: Core ETL logic (Pandas/SQLAlchemy).

**requirements.txt**: Managed dependency list.

**.gitignore**: Pre-configured to exclude sensitive keys and database volumes.