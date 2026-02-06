
# 🚀 Day 10: The Streaming Lakehouse (CE Edition)

**Phase:** Week 2 Weekend (The Build)  
**Focus:** Spark Structured Streaming, Backpressure, "Spike" Handling, and Binary Search Trees.  
**Constraint:** Databricks Community Edition (Standard Streams, No Autoscaling).  
**Estimated Time:** 4 Hours (Deep Work)  

---

## 🎯 Objectives
1.  **Engineering Implementation:** Build a real-time ingestion pipeline using **Standard Structured Streaming** (adapted for Community Edition restrictions).
2.  **System Design:** Master the "Senior" answer to **"How do you handle massive data spikes?"** (Backpressure & Flow Control).
3.  **Algorithmic Proficiency:** Master **Binary Search Trees (BST)**, the foundational data structure for Database Indexing.

---

## 🏗️ Phase 1: System Design (The "Spike" Scenario)
**Context:** Interview Preparation  
**Question:** *"Your system normally handles 1k events/sec. Suddenly, it hits 100k events/sec. How do you ensure the driver doesn't crash (OOM) and eventually processes the backlog?"*

**Action:** In `docs/Week2/Day10/JOURNAL.md`, write a section **"Handling Streaming Spikes"** covering these three layers of defense:

1.  **Protection (Backpressure):** * Explain `spark.streaming.backpressure.enabled`.
    * *Concept:* Spark estimates the ingestion rate vs. processing rate and dynamically reduces the receiving rate so the driver doesn't explode.
2.  **Control (Batch Size):** * Explain `maxFilesPerTrigger` (or `maxOffsetsPerTrigger`).
    * *Concept:* Capping the input per micro-batch ensures predictable execution time even during a flood.
3.  **Scale (Elasticity):** * Explain **Cluster Autoscaling** (Theoretical for CE).
    * *Concept:* Adding worker nodes to chew through the backlog (requires sufficient Source Partitions).

---

## 🛠️ Phase 2: Project 2 — Streaming Ingestion
**Context:** "Retail360" Real-Time Layer  
**Repo Path:** `project2_streaming/notebooks/04_stream_bronze.py`

**Task:** Implement a stream that simulates "Spike Protection" by forcing a small batch size.

### Code Specification
Since `cloudFiles` (Auto Loader) is unavailable in CE, use **Standard Streaming**:

1.  **Explicit Schema:** You must define `StructType` manually for CSV streaming.
2.  **Flow Control:** Set `.option("maxFilesPerTrigger", 1)` to simulate a throttled ingestion.
3.  **Checkpointing:** Essential for fault tolerance.
4.  **Trigger:** Use `.trigger(availableNow=True)` for cost-effective micro-batching.

```python
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, TimestampType

# 1. Define Schema (Mandatory for CE CSV Streaming)
bronze_schema = StructType([
    StructField("InvoiceNo", StringType(), True),
    StructField("StockCode", StringType(), True),
    StructField("Description", StringType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("InvoiceDate", StringType(), True),
    StructField("UnitPrice", DoubleType(), True),
    StructField("CustomerID", DoubleType(), True),
    StructField("Country", StringType(), True)
])

# 2. Source: The "Throttled" Stream
raw_stream = (
    spark.readStream
    .format("csv")
    .schema(bronze_schema)
    .option("header", "true")
    .option("maxFilesPerTrigger", 1)  # <--- The "Control" mechanism
    .load("dbfs:/FileStore/raw/retail/")
)

# 3. Add Metadata (Lineage)
enhanced_stream = (
    raw_stream
    .withColumn("_ingest_timestamp", F.current_timestamp())
    .withColumn("_source_file", F.input_file_name())
)

# 4. Sink: Append to Delta with Checkpointing
query = (
    enhanced_stream.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "dbfs:/FileStore/checkpoints/bronze_stream_retail")
    .trigger(availableNow=True)
    .table("bronze_stream_retail")
)

query.awaitTermination()

```

---

## 📐 Phase 3: Algorithmic Engineering (DSA)

**Context:** Binary Search Trees (BST)

### 1. Validate Binary Search Tree (LeetCode #98)

* **Pattern:** Recursion with Range.
* **Logic:** A node is valid only if `min_val < node.val < max_val`. Pass updated ranges down to children.

### 2. Kth Smallest Element in a BST (LeetCode #230)

* **Pattern:** In-Order Traversal.
* **Logic:** In-order traversal (`Left -> Root -> Right`) visits BST nodes in sorted ascending order. Stop at the -th visited node.

### 3. Lowest Common Ancestor of a BST (LeetCode #235)

* **Pattern:** BST Property Navigation.
* **Logic:** If `p` and `q` are both smaller than root, go Left. If both larger, go Right. Otherwise, current root is the LCA.

---

## 📝 Deliverables & Verification

### Repository Sync

* **Location:** `data-engineering-portfolio-2026`
* **Checklist:**
* [ ] `project2_streaming/notebooks/04_stream_bronze.py` (Streaming Logic).
* [ ] `dsa/day10/` (BST Solutions).
* [ ] `docs/Week2/Day10/JOURNAL.md` (Spike Handling Explanation).



### ✅ Verification Question

> *In standard Structured Streaming (what you just wrote), if I add a new column to the CSV file but don't update the `StructType` in my code, what happens to that new data column during ingestion?*


---