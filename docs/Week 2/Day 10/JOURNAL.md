# 📘 Week 2 — Day 10 Journal  

**Date:** 03/01/2026

----
## 🏗️ Phase 1: System Design (The "Spike" Scenario)

Analyzed architectural strategies to handle a sudden spike in streaming traffic (e.g., 1k events/sec → 100k events/sec) while maintaining system stability.

### 1. Durable Buffer
Reviewed the use of a distributed message queue (e.g., Kafka) to decouple producers and consumers.

Compared architectures:
- Existing: `producer → processor → sink`
- Proposed: `producer → message queue → consumer → sink`

Understood that a durable buffer absorbs incoming spikes, enables replay capability, and separates ingestion from processing.

### 2. Horizontal Scaling
Studied scaling strategies across streaming components:

- Increased the number of Kafka consumer instances.
- Increased Spark Structured Streaming executors.
- Observed that micro-batch parallelism influences overall throughput.

### 3. Partitioning Strategy
Reviewed the role of partitioning in enabling horizontal scaling.

- Each partition can be processed independently by a consumer.
- Higher partition counts allow higher parallelism.
- Considered over-provisioning partitions based on expected peak load to support future scaling.

### 4. Backpressure & Flow Control
Explored built-in flow control mechanisms in Spark Structured Streaming:

- Rate limiting.
- `maxOffsetsPerTrigger`.
- Controlled batch sizing via configuration.

Understood how these mechanisms prevent the processing engine from being overwhelmed during spikes.

### 5. Idempotent Sink Design
Reviewed strategies to prevent duplication or data corruption at the sink layer.

- Leveraged Delta Lake’s transactional guarantees.
- Used primary key–based `MERGE` operations to ensure deterministic writes.

### 6. Monitoring & Alerting
Identified key operational metrics to monitor during high-load scenarios:

- Queue depth.
- Processing latency.
- Error rates.

Considered configuring alerts based on threshold breaches for proactive system management.

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
