# People Medallion Pipeline

A **Medallion Architecture (Bronze → Silver → Gold)** data pipeline built using **Databricks Delta Live Tables (DLT)**, ingesting and transforming people demographic data through progressively refined layers.

##  Architecture

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   BRONZE    │  →   │   SILVER    │  →   │    GOLD     │
│  Raw Data   │      │  Cleaned &  │      │  Business   │
│  (as-is)    │      │  Validated  │      │ Aggregates  │
└─────────────┘      └─────────────┘      └─────────────┘
```

| Layer | Purpose | Description |
|-------|---------|-------------|
| **Bronze** | Raw ingestion | Streams raw CSV files from a Databricks Volume as-is, with an added `ingestion_time` column for auditability. |
| **Silver** | Cleaning & validation | Selects relevant columns, drops duplicate records (by `Phone`, `Email`, `User_Id`). |
| **Gold** | Business-ready aggregates | Produces summary tables: gender distribution and top job titles. |

##  Dataset

Source: `people-100.csv` — 100 synthetic records with the following columns:

`Index, User_Id, First_Name, Last_Name, Sex, Email, Phone, Date_of_birth, Job_Title`

##  Tech Stack

- **Databricks** (Delta Live Tables / DLT)
- **PySpark** (Structured Streaming - `readStream` / `cloudFiles` Auto Loader)
- **Delta Lake** for storage
- **Unity Catalog Volumes** for raw file landing

##  Project Structure

```
people-medallion-pipeline/
├── notebooks/
│   └── people_pipeline.py       # DLT pipeline: bronze, silver, gold tables
├── data/
│   └── people-100.csv           # Sample source data
├── README.md
└── LICENSE
```

##  Pipeline Details

### Bronze — `people_bronze`
Streams raw CSV files from a Volume using Auto Loader (`cloudFiles`), tagging each record with an `ingestion_time` timestamp. No transformations applied.

### Silver — `people_silver`
Reads from Bronze, selects core columns (`User_ID`, `Email`, `Phone`, `Date_of_birth`, `Job_Title`), and removes duplicate records.

### Gold — Aggregate Tables
- **`people_gold_gender_summary`** — count per gender
- **`people_gold_job_title_counts`** — top 10 most common job titles
##  How to Run

1. Upload `people-100.csv` to a Unity Catalog Volume:
   ```
   /Volumes/<catalog>/<schema>/<volume>/people/
   ```
2. Create a new **DLT Pipeline** in Databricks and point it to `notebooks/people_pipeline.py`.
3. Set the pipeline mode to **Triggered** or **Continuous** as needed.
4. Run the pipeline — Bronze, Silver, and Gold tables will be created automatically in the target schema.


##  Notes

- This is a **practice / learning project** demonstrating the Medallion Architecture pattern using Databricks DLT.
- Dataset is synthetic and used for demonstration purposes only.

##  License

This project is licensed under the MIT License.
