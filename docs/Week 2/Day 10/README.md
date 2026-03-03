# 🚀 Day 10: The Streaming Lakehouse

**Phase:** Week 2 — Real-Time Systems  
**Focus:** Spark Structured Streaming, Backpressure, and Binary Search Trees.  
**Estimated Time:** 4 Hours (Deep Work)  

---

## 🎯 Objectives
1.  **Engineering Implementation:** Build a real-time ingestion pipeline using **Standard Structured Streaming** with explicit flow control.
2.  **System Design:** Master the architectural strategies for handling massive data spikes by defining layers of defense: Backpressure, Batch Capping, and Load Shedding.
3.  **Algorithmic Proficiency:** Master **Binary Search Trees (BST)**, the foundational structure for database indexing and sorted data retrieval.

---

## 🏗️ Phase 1: System Design (The "Spike" Scenario)
**Context:** Technical Architecture Review  
**Question:** *"A system normally processes 1k events/sec. Suddenly, the load increases to 100k events/sec. How do you prevent a system crash and ensure all data eventually reaches the sink?"*

**Action:** In your `JOURNAL.md`, create a section titled **"Handling Streaming Spikes"** covering these three layers:

1.  **Backpressure:** Explain `spark.streaming.backpressure.enabled`. This allows the system to signal the data source to slow down, preventing the processing engine from being overwhelmed.
2.  **Batch Capping:** Explain `maxFilesPerTrigger` or `maxOffsetsPerTrigger`. This sets a hard limit on the amount of data pulled in a single micro-batch, ensuring predictable execution times.
3.  **Elasticity:** Discuss Cluster Autoscaling—dynamically adding compute resources to increase throughput and clear backlogs once the system is stabilized.

---

## 🛠️ Phase 2: Project 2 — Streaming Ingestion
**Context:** "Retail360" Real-Time Layer  
**Task:** Implement a stream that utilizes a controlled batch size to maintain stability.

### Code Specification
Implement the logic in `project2_streaming/notebooks/04_stream_bronze.py`:

```python
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# 1. Define Explicit Schema
bronze_schema = StructType([
    StructField("InvoiceNo", StringType(), True),
    StructField("StockCode", StringType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("InvoiceDate", StringType(), True),
    StructField("UnitPrice", DoubleType(), True),
    StructField("CustomerID", DoubleType(), True)
])

# 2. Source: The Throttled Stream
raw_stream = (
    spark.readStream
    .format("csv")
    .schema(bronze_schema)
    .option("header", "true")
    .option("maxFilesPerTrigger", 1)  # Flow control mechanism
    .load("dbfs:/FileStore/raw/retail/")
)

# 3. Sink: Append to Delta with Checkpointing
query = (
    raw_stream.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "dbfs:/FileStore/checkpoints/bronze_stream")
    .trigger(availableNow=True)
    .table("bronze_stream_retail")
)

```

---

## 📐 Phase 3: Algorithmic Engineering (DSA)

**Context:** Binary Search Trees (BST)

1. **Validate Binary Search Tree (LeetCode #98):** Verify the tree property where left < root < right.
2. **Lowest Common Ancestor of a BST (LeetCode #235):** Use the BST property to find the split point between two nodes.
3. **Kth Smallest Element in a BST (LeetCode #230):** Implement an In-Order traversal to visit nodes in sorted order.

---

## 📝 Deliverables & Verification

### ✅ Verification Questions

1. **Logic Check:** In a sustained 10x spike, why is a message buffer (like a queue) insufficient as a standalone solution for system stability?
2. **State Management:** If you delete the `checkpointLocation` directory of an active stream and restart the job, what happens to the data that was already successfully processed?

---
