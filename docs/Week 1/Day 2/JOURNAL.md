# 📘 Week 1 — Day 2 Journal  

**Date:** 14/12/2025

----

## Phase 1 — Algorithmic Engineering (DSA)

### 1.1. Two Sum (#1)
Solved using a hash-based approach.  
Iterated through the array while storing the expected complement (`target - current value`) in an unordered_map.  
When the current element matched a previously stored complement, returned the corresponding indices.

### 1.2. Top K Frequent Elements (#347)
Computed element frequencies using an unordered_map.  
Implemented two approaches:
- Grouped elements by frequency using an ordered map to retrieve the most frequent values.
- Used a min-heap (priority queue) of fixed size `k` to track the top `k` frequent elements without sorting the entire dataset.

Tested the solutions with varying input sizes and frequency distributions.

### 1.3. Product of Array Except Self (#238)
Implemented prefix and suffix product logic to compute the product of all elements except the current index in O(n) time without using division.  
Also implemented an optimized version that stores prefix products directly in the result array and applies suffix products using a single running variable to reduce extra space usage.

----

## Phase 2 — Platform Architecture (Databricks Associate)

### 2.2.1. Delta Log and ACID Transactions
Created a new schema `lab_2026` and a Delta table named `events` with columns `id` and `data` using Spark SQL.

Verified table metadata using `DESC FORMATTED events`.

Performed multiple INSERT operations on the Delta table:
- Inserted `(1, 'click')`
- Inserted `(2, 'view')`
- Inserted `(3, 'purchase')`

Each INSERT was executed as a separate transaction.

### 2.2.2. Delta Log Inspection and Time Travel
Inspected the transactional history of the Delta table using `DESCRIBE HISTORY events`.

Observed that:
- Each INSERT operation is recorded as an individual transaction.
- Delta maintains an ordered history of table versions corresponding to these transactions.

Noted that Delta Lake does not modify existing data files in place. Instead, transactional changes are captured through metadata entries in the Delta log, enabling reconstruction of table state for any version.

### 2.3. Medallion Architecture

Reviewed the Medallion Architecture pattern and documented the purpose of each layer:

- **Bronze Layer:**
  - Stores raw ingested data.
  - Append-only with no filtering or transformations applied.
  - Retains full historical data.

- **Silver Layer:**
  - Contains cleaned and filtered data.
  - Maintains historical records.
  - Acts as the single source of truth for downstream processing.

- **Gold Layer:**
  - Stores aggregated and curated datasets.
  - Designed for business-level consumption and analytics.

----

## Phase 3 — System Internals (Storage Design)

### 3.4. Parquet Internals & Data Skipping
Reviewed how Parquet stores column-level statistics such as minimum and maximum values.

Observed that if a Parquet file has `ID_min = 100` and `ID_max = 200`, a query like  
`SELECT * FROM table WHERE id = 50`  
skips this file entirely because the filter value does not fall within the stored range.

This behavior is part of the data skipping mechanism in columnar storage formats, allowing the query engine to avoid reading unnecessary files and improving query performance.

----

## Phase 4 — GenAI

### 4.5. GenAI Lab: Tokenization

Installed and imported the `tiktoken` library and loaded the `cl100k_base` tokenizer.

Performed tokenization on different input types:
- A short word: `"Data"`
- A numeric string: `"794625452451"`

Observed the following results:
- `"Data"` was encoded as a single token.
- `"794625452451"` was encoded into multiple tokens.

Captured token counts:
- Word token count: 1
- Number token count: 4

Also tokenized a timestamp string (`"2024-09-18T12:45:33Z"`) to observe how structured numeric and symbolic data is split into tokens.

Noted that numerical and structured strings consume more tokens compared to common natural language words due to how tokenizers segment less frequent patterns.

----

# ✔️ Day 2 Status: _CLEARED_
