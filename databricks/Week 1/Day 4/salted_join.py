# Databricks notebook source
# MAGIC %md
# MAGIC ## Step 1: Data Preparation (Skew Simulation)
# MAGIC
# MAGIC We prepare two datasets:
# MAGIC - A **small lookup table** (`df_small`)
# MAGIC - A **large fact table** (`df_large`) with intentionally skewed `user_id` distribution
# MAGIC
# MAGIC This setup helps demonstrate how skew impacts joins in Spark.

# COMMAND ----------

from pyspark.sql import functions as F, types as T

df_small = (
    spark
    .range(100)
    .withColumn('group', F.concat_ws('_', F.lit('group'), F.round(F.col('id') * F.rand() * 10) % 10 ))
    .withColumnRenamed('id', 'user_id')
)

df_small.groupBy('group').agg(F.collect_set(F.col('user_id'))).display()

# COMMAND ----------

df_large1 = (
    spark
    .range(100000)
    .withColumn('user_id', F.floor((F.col('id') * F.rand() * 100) + F.rand() * 100) % 60)
    .withColumn('value', F.rand())
    .withColumnRenamed('id', 'transaction_id')
)

df_large2 = (
    spark
    .range(100)
    .withColumn('user_id', 60 + F.round((F.col('id') * F.rand())) % 40)
    .withColumn('value', F.rand())
    .withColumnRenamed('id', 'transaction_id')
)

df_large = (
    df_large1
    .union(df_large2)
)

df_large.groupBy('user_id').count().display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Baseline Join (Skewed Join Behavior)
# MAGIC
# MAGIC We perform a standard join on `user_id` to illustrate the skew problem.
# MAGIC Highly frequent `user_id` values cause data to concentrate in a few partitions,
# MAGIC leading to uneven task execution and performance bottlenecks.

# COMMAND ----------

df_small.join(df_large, ['user_id'], 'inner').groupBy('group', 'user_id').count().display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Salted Join (Skew Mitigation)
# MAGIC
# MAGIC To mitigate join skew, we apply the **salting technique**:
# MAGIC - Split a hot join key into multiple artificial keys
# MAGIC - Force Spark to redistribute the workload across executors

# COMMAND ----------

N = 10

# COMMAND ----------

# MAGIC %md
# MAGIC ### Prepare Salted DataFrames
# MAGIC
# MAGIC - **Large table:** Add a random `salt` column (0 to N-1)  
# MAGIC - **Small table:** Duplicate each row across all possible salt values
# MAGIC
# MAGIC This ensures that each salted key has a matching row during the join.
# MAGIC

# COMMAND ----------

df_small_salted = (
  df_small
  .withColumn("salt", F.explode(F.array([F.lit(i) for i in range(N)])))
)

df_small_salted.limit(10).display()

# COMMAND ----------

df_large_salted = (
    df_large
    .withColumn('salt', F.floor(F.rand() * N))
)

df_large_salted.limit(10).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Join Using Composite Key (user_id, salt)
# MAGIC
# MAGIC We now join using both `user_id` and `salt`.
# MAGIC This distributes previously skewed keys across multiple partitions,
# MAGIC significantly reducing hotspot executors and improving parallelism.
# MAGIC

# COMMAND ----------

(
  df_large_salted
  .join(df_small_salted, ["user_id", "salt"], "inner")
  .groupBy("user_id", "salt")
  .count()
  .display()
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Conclusion
# MAGIC > Salting mitigates join skew by artificially splitting hot keys into multiple partitions,
# MAGIC forcing Spark to parallelize processing instead of overloading a single executor.
# MAGIC