# 📘 Week 1 — Day 7 Journal  

**Date:** 02/01/2026

----
## 🏗️ Phase 1: The Silver Layer (Clean & Upsert)

Implemented a transformation pipeline to clean and upsert data from the Bronze layer into the Silver Delta table.

Read data from the Bronze table and explicitly cast columns to appropriate data types, including numeric, decimal, and timestamp fields.

Applied a deduplication strategy using a window function partitioned by `invoice` and `stockcode`, ordered by `invoicedate` and ingestion timestamp.  
Retained only the most recent record per `(invoice, stockcode)` combination.

Removed ingestion-related metadata after deduplication to maintain a clean Silver schema.

Performed an upsert operation using `DeltaTable.merge()`:
- Matched records based on `invoice` and `stockcode`.
- Updated existing records when a match was found.
- Inserted new records when no match existed.

Captured insert and update timestamps to track data changes over time.

----
## 📊 Phase 2: The Gold Layer (Business Aggregates)

Built a Gold-layer aggregation model to generate daily sales metrics for analytics use cases.

Read cleaned data from the Silver table and derived a date column from the invoice timestamp.

Aggregated data by `country` and `invoice_date` to compute:
- Total revenue as the sum of `price * quantity`.
- Total orders as the distinct count of invoices.

Added insert and update timestamps to the aggregated dataset.

Applied an upsert strategy using `DeltaTable.merge()` to maintain the Gold table:
- Matched records on `country` and `invoice_date`.
- Updated revenue and order metrics for existing records.
- Inserted new daily aggregates when no matching record was found.

----
## 🛠️ Phase 3: Algorithmic Engineering (DSA)

### 1. Number of Islands (LeetCode #200)
Implemented a Depth First Search (DFS) approach to count the number of islands in a 2D grid.

Iterated through each cell of the grid and initiated a DFS whenever an unvisited land cell was encountered.  
Marked connected land cells as visited by modifying the grid in place to avoid revisiting the same island.  
Counted each DFS initiation as a distinct island.

### 2. Implement Queue using Stacks (LeetCode #232)
Implemented a queue using two stacks.

Explored two approaches:
- A push-heavy approach where elements are reordered during each enqueue operation to maintain FIFO order.
- An optimized approach using separate input and output stacks, transferring elements only when required during dequeue or peek operations.

Verified queue behavior by testing enqueue, dequeue, peek, and empty operations.

----
## 🤖 Phase 4: GenAI "Hello Vector"

Implemented a basic end-to-end vector database workflow using Pinecone.

Installed and imported the Pinecone client library and initialized the client using an API key provided through environment variables.

Created a serverless Pinecone index named `day7-hello-vector` with:
- Vector dimension set to 3
- Cosine similarity as the distance metric
- AWS as the cloud provider and `us-east-1` as the region

Connected to the created index and upserted a dummy vector with an associated metadata payload.

Executed a similarity query against the index using a query vector and retrieved the closest matching vector along with its metadata to validate end-to-end connectivity and query functionality.

----
## Verification Question

**Question:**  
*In the Silver Layer, if I receive a record with the same `InvoiceNo` but a different `Quantity` than what is currently in the table, what specific Delta command ensures the record is updated rather than duplicated?*

**Answer:**  
- The `DeltaTable.merge()` command is used to perform an upsert operation. When a matching condition is satisfied, the existing record is updated; when no match is found, a new record is inserted.
- The same `merge` operation can also be configured to delete records when a match condition is met.

----

# ✔️ Day 7 Status: _CLEARED_
