# 📘 Week 2 — Day 10 Journal  

**Date:** 03/01/2026

----
## 🏗️ Phase 1: System Design (The "Spike" Scenario)

### 1. Backpressure
### 2. Batch Capping
### 3. Elasticity

----
## 🛠️ Phase 2: Project 2 — Streaming Ingestion

### 1. The Stream Source (Controlled Structured Streaming)

Implemented a structured streaming ingestion pipeline using an explicitly defined schema for the Bronze layer.

Defined a `StructType` schema for incoming retail CSV files to avoid schema inference during streaming.

Configured the streaming source using:

- `format("csv")`
- `.schema(bronze_schema)`
- `.option("header", "true")`
- `.option("maxFilesPerTrigger", 1)` to limit the number of files processed per micro-batch

Loaded files from:
`dbfs:/FileStore/raw/retail/`

Configured the sink to write data in append mode to a Delta table:

- `.format("delta")`
- `.outputMode("append")`
- `.option("checkpointLocation", "dbfs:/FileStore/checkpoints/bronze_stream")`
- `.trigger(availableNow=True)`

Persisted the stream output to the Delta table:
`bronze_stream_retail`

Observed that the stream processed available files in controlled micro-batches and terminated automatically due to `availableNow=True`.

### 2. Checkpointing & State Tracking

Configured a dedicated checkpoint directory to track streaming progress and processed file metadata.

Verified that Spark maintains stream state in the checkpoint location to ensure fault tolerance and recovery.

Confirmed that previously processed files are not reprocessed when the stream is restarted, as long as the checkpoint directory remains intact.

----
## 📐 Phase 3: Algorithmic Engineering (DSA)

### 1. Validate Binary Search Tree (LeetCode #98)
Implemented a solution to validate whether a binary tree satisfies Binary Search Tree properties.

Performed an in-order traversal of the tree to collect node values.  
Verified that the traversal sequence is strictly increasing to confirm BST validity.  
Handled null nodes appropriately during traversal.
### 2. Lowest Common Ancestor of a BST (LeetCode #235)
Implemented an in-order traversal approach to find the k-th smallest element in a Binary Search Tree.

Traversed the tree in sorted order and stored node values in a list.  
Returned the element at the k-th position using 1-based indexing.
### 3. Kth Smallest Element in a BST (LeetCode #230)
Implemented logic to find the lowest common ancestor of two nodes in a Binary Search Tree.

Used BST ordering properties to traverse the tree:
- Moved left when both target nodes were smaller than the current node.
- Moved right when both target nodes were larger than the current node.
- Identified the current node as the lowest common ancestor when the targets diverged across subtrees.

Applied the approach until the ancestor node was found.

----
## Verification Question

**Question:**  
*If I delete the `checkpoint` directory of a running streaming job, what happens when I restart the job?*

**Answer:**  

----

# ✔️ Day 10 Status: _TO-DO_
