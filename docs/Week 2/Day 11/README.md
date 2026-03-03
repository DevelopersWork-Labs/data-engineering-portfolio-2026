### 🚀 Day 11: Stateful Streaming & Precision DSA

**Phase:** Week 2 — Advanced System Control

**Focus:** Event-Time Processing, Watermarking, and Balanced Search Trees.

**Estimated Time:** 4 Hours (Deep Work)

---

## 🎯 Objectives

1. **Engineering Implementation:** Implement **Watermarking** and **Windowed Aggregations** to handle late-arriving data in the real-time pipeline.
2. **System Design:** Master the concept of **Exactly-Once Semantics (EOS)** and how checkpoints/idempotent sinks prevent data duplication.
3. **Algorithmic Proficiency:** Understand **Tree Balancing** (AVL/Red-Black logic) to bridge the gap between basic BSTs and production database indexing.

---

## 🏗️ Phase 1: System Design (The "Exactly-Once" Challenge)

**Context:** Technical Architecture Review

**Question:** *"If a streaming job crashes mid-batch after writing some data but before updating the checkpoint, how do you prevent duplicate records upon restart?"*

**Action:** In your `JOURNAL.md`, create a section titled **"Streaming Reliability Patterns"** covering:

1. **Exactly-Once Semantics (EOS):** Explain how Spark uses the write-ahead log (WAL) and checkpoints to track offsets.
2. **Idempotent Sinks:** Discuss why Delta Lake is uniquely suited for this, as it handles concurrent commits and ensures that a re-processed batch doesn't create duplicate entries.
3. **Watermarking:** Explain how `withWatermark` allows the system to automatically drop state for data that is "too late," preventing unbounded state store growth.

---

## 🛠️ Phase 2: Project 2 — Stateful Transformations

**Context:** "Retail360" Analytical Layer

**Task:** Enhance the Bronze-to-Silver stream to calculate a rolling count of invoices using event-time windows.

### Code Specification

Implement the logic in `project2_streaming/notebooks/05_stream_silver_aggregations.py`:

```python
from pyspark.sql import functions as F

# 1. Read from the Bronze Delta Table as a Stream
bronze_df = spark.readStream.table("bronze_stream_retail")

# 2. Apply Watermarking and Windowing
# Use 'InvoiceDate' as the event time; allow 10 minutes of lateness
windowed_counts = (
    bronze_df
    .withColumn("timestamp", F.to_timestamp("InvoiceDate", "d/M/yyyy H:mm"))
    .withWatermark("timestamp", "10 minutes") 
    .groupBy(
        F.window("timestamp", "5 minutes"),
        "Country"
    )
    .count()
)

# 3. Sink: Write to a specialized Silver Aggregation table
query = (
    windowed_counts.writeStream
    .format("delta")
    .outputMode("complete") # Required for aggregations
    .option("checkpointLocation", "dbfs:/FileStore/checkpoints/silver_agg_retail")
    .table("silver_invoice_counts")
)

```

---

## 📐 Phase 3: Algorithmic Engineering (DSA)

**Context:** Balanced Search Trees

1. **Balanced Binary Tree (LeetCode #110):** Implement a solution to check if a tree is height-balanced (difference between subtrees <= 1).
2. **Convert Sorted Array to Binary Search Tree (LeetCode #108):** Given a sorted array, create a height-balanced BST. This is the logic used to build efficient range-query indices.
3. **Concept Review:** Research why **B-Trees** (a variation of balanced trees) are used for disk-based storage in databases rather than standard BSTs.

---

## 📝 Deliverables & Verification

### ✅ Verification Questions

1. **State Management:** What happens to the "State Store" if you set a watermark of 10 minutes but data arrives 15 minutes late?
2. **Output Modes:** Why is `outputMode("append")` usually not allowed for streaming aggregations unless a watermark is defined?

---

