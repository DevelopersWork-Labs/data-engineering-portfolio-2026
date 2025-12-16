# Databricks notebook source
# MAGIC %md
# MAGIC Understand how Delta Lake gives ACID guarantees on top of plain object storage (S3/DBFS).
# MAGIC
# MAGIC Delta does NOT modify files. It logs what happened.
# MAGIC
# MAGIC That log = `_delta_log`.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Create a Delta Table

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS lab_2026;
# MAGIC USE lab_2026;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE events (
# MAGIC   id INT,
# MAGIC   data STRING
# MAGIC ) USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESC FORMATTED events;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Insert Data

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO events VALUES (1, 'click');
# MAGIC INSERT INTO events VALUES (2, 'view');
# MAGIC INSERT INTO events VALUES (3, 'purchase');

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Inspect Delta Log

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY events;