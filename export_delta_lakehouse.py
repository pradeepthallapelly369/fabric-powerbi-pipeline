#!/usr/bin/env python3
"""
Delta Lakehouse Pipeline for Microsoft Fabric & Databricks
Pradeep Thallapelly — Global Career AI Engine

Exports career pipeline tables to open Delta Lake format (Parquet + _delta_log)
compatible with:
1. Microsoft Fabric OneLake & Direct Lake Power BI Mode
2. Databricks Unity Catalog & Delta Tables
3. SemPy (Semantic Link) automated DAX evaluation
"""

import os
import sys
import pandas as pd
from deltalake import write_deltalake, DeltaTable
from datetime import datetime

PIPELINE_ROOT = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.dirname(os.path.dirname(PIPELINE_ROOT))
PBI_DATA_DIR = "/home/upc/every_thing_claude/powerbi_data"
DELTA_DIR = os.path.join(PBI_DATA_DIR, "delta_lakehouse")

os.makedirs(DELTA_DIR, exist_ok=True)

def export_delta_tables():
    print("="*75)
    print("🧊 DELTA LAKEHOUSE EXPORT FOR FABRIC & DATABRICKS")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}")
    print(f"Source: {PBI_DATA_DIR}")
    print(f"Destination: {DELTA_DIR}")
    print("="*75)

    tables = [
        ("Fact_Applications.csv", "fact_applications"),
        ("Fact_ColdEmails.csv", "fact_cold_emails"),
        ("Dim_Jobs.csv", "dim_jobs"),
        ("Dim_Contacts.csv", "dim_contacts"),
        ("Dim_Date.csv", "dim_date"),
    ]

    for csv_file, table_name in tables:
        csv_path = os.path.join(PBI_DATA_DIR, csv_file)
        if not os.path.exists(csv_path):
            print(f"[-] Missing {csv_file}, skipping.")
            continue

        table_path = os.path.join(DELTA_DIR, table_name)
        df = pd.read_csv(csv_path)

        # Write as Delta table (mode='overwrite' ensures clean idempotency)
        write_deltalake(table_path, df, mode="overwrite")
        dt = DeltaTable(table_path)
        print(f"✅ Delta Table '{table_name}': {len(df)} rows | Version {dt.version()} -> {table_path}")

    # Generate Databricks & Fabric DDL helper script
    ddl_path = os.path.join(DELTA_DIR, "lakehouse_schema.sql")
    with open(ddl_path, "w", encoding="utf-8") as f:
        f.write(f"""-- =============================================================================
-- Microsoft Fabric & Databricks Delta Lakehouse DDL
-- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}
-- =============================================================================

-- 1. Create Schema / Database
CREATE DATABASE IF NOT EXISTS career_analytics;
USE career_analytics;

-- 2. Fact Applications
CREATE TABLE IF NOT EXISTS fact_applications
USING DELTA
LOCATION '{os.path.join(DELTA_DIR, "fact_applications")}';

-- 3. Fact Cold Emails
CREATE TABLE IF NOT EXISTS fact_cold_emails
USING DELTA
LOCATION '{os.path.join(DELTA_DIR, "fact_cold_emails")}';

-- 4. Dim Jobs
CREATE TABLE IF NOT EXISTS dim_jobs
USING DELTA
LOCATION '{os.path.join(DELTA_DIR, "dim_jobs")}';

-- 5. Dim Contacts
CREATE TABLE IF NOT EXISTS dim_contacts
USING DELTA
LOCATION '{os.path.join(DELTA_DIR, "dim_contacts")}';

-- 6. Dim Date
CREATE TABLE IF NOT EXISTS dim_date
USING DELTA
LOCATION '{os.path.join(DELTA_DIR, "dim_date")}';
""")
    print(f"✅ Generated Lakehouse DDL script -> {ddl_path}")
    print("\n" + "="*75)
    print("🏁 DELTA LAKEHOUSE EXPORT COMPLETE!")
    print("="*75)

if __name__ == "__main__":
    export_delta_tables()
