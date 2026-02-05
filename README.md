
# 📦 FileUploaderToPostgres

A **Python-based data ingestion utility** that automatically reads CSV and Excel files from a directory and uploads them into a PostgreSQL database with logging, error handling, and scalable batch inserts.

---

## 🚀 Features

* 📂 Auto-detects **CSV / Excel** files from a data folder
* 🧹 Cleans and normalizes table names automatically
* 🛢 Uploads data into **PostgreSQL** using SQLAlchemy
* ➕ **Appends data** to existing tables (no overwrites)
* 📊 Handles large files with chunked batch inserts
* 📝 Centralized logging (file + optional console)
* 🔐 Secure DB connection via config file

---

## 📁 Project Structure

```text
FileUploaderToPostgress/
│
├── data/                  # Input data files (.csv, .xlsx)
│
├── logs/                  # Auto-generated log files
│   └── inventory_ingest.log
│
├── utils/
│   ├── db_config.py       # Database engine configuration
│   ├── ingestion.py       # Data ingestion logic
│   ├── log_config.py      # Logger configuration
│   └── __pycache__/
│
├── uploader.ipynb         # Main ingestion runner (Notebook)
└── README.md              # Project documentation
```

---

## ⚙️ Prerequisites

Make sure you have the following installed:

* Python **3.9+**
* PostgreSQL
* pip / conda

### Required Python Packages

```bash
pip install pandas sqlalchemy psycopg2-binary openpyxl
```

---

## 🔐 Database Configuration

Update the database connection in `uploader.ipynb` or environment variable:

```python
DB_URL = "postgresql://username:password@host:port/database"
```

Example:

```python
postgresql://postgres:password@localhost:5432/blinkit_db
```

> ⚠️ **Do NOT commit credentials** — keep `db_config.py` ignored in `.gitignore`.

---

## ▶️ How It Works

1. Place CSV / Excel files inside the `data/` folder
2. File names are converted into **table names**

   * Spaces & symbols → `_`
   * Lowercased automatically
3. Tables are created if they don’t exist
4. Data is **appended**, not overwritten
5. Logs are written to `logs/`

---

## 🧠 Core Logic Overview

### File Detection

```python
SUPPORTED_EXTENSIONS = (".csv", ".xlsx", ".xls")
```

### Table Name Cleaning

```python
orders-data.xlsx → orders_data
```

### Ingestion Strategy

```python
df.to_sql(
    if_exists="append",
    chunksize=10000,
    method="multi"
)
```

✔ Efficient
✔ Scalable
✔ Safe for production use

---

## 📝 Logging

* Logs stored in `logs/<logger_name>.log`
* Includes timestamps, levels, and messages
* Console logging optional

Example log:

```text
2026-02-05 14:22:10 | INFO | inventory_ingest | Appended 12000 rows into orders
```

---

## ❌ Error Handling

* Each file is processed independently
* Errors are logged without stopping the pipeline
* Full stack trace captured for debugging

---

## 🧪 Example Usage

```bash
# Activate environment
conda activate base

# Run notebook
jupyter notebook uploader.ipynb
```

OR convert to script later for cron / automation.

---

## 🔮 Future Enhancements

* ✅ Schema validation
* ⏱ Incremental loading
* 🔁 Duplicate detection
* ☁️ Cloud storage (S3 / GCS)
* 🐳 Docker support
* 📈 Data quality checks

---
Built by Kshitij Singh

