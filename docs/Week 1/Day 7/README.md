# 🚀 Day 7: The Silver & Gold Refineries

**Phase:** Week 1 Weekend (The Build - Part 2)  
**Focus:** ACID Merges (Upserts), Business Aggregations, and Vector Database Connectivity.  
**Type:** 5-Hour Workshop (Deep Work)  

---

## 🎯 Objectives
1.  **Production Data Engineering:** Complete the "Retail360" Lakehouse by building the **Silver** (Clean & Upsert) and **Gold** (Aggregated) layers.
2.  **Architecture:** Implement **SCD Type 1 (Upsert)** logic using Delta Lake's `MERGE` command and optimize query performance with `Z-ORDER`.
3.  **Algorithmic Proficiency:** Master Graph Traversal (BFS/DFS) and Queue design patterns.
4.  **GenAI Infrastructure:** Establish a working connection to a Vector Database (Pinecone/Chroma) to prepare for RAG.

---

## 🏗️ Phase 1: The Silver Layer (Clean & Upsert)
**Context:** Deduplication and Quality Enforcement  
**Repo Path:** `project1_lakehouse/notebooks/02_transform_silver.py`

### 1. Data Cleaning
* **Requirement:** Filter out invalid records from the Bronze layer.
    * Rule: `Quantity > 0` AND `UnitPrice > 0`.
    * *Why:* Negative values in retail usually indicate returns or errors, which we handle separately or exclude from sales analysis.

### 2. The MERGE Operation (Upsert)
* **Logic:** We cannot just append to Silver; we must handle updates.
* **Command:** Use `DeltaTable.merge()`.
* **Match Condition:** `target.Invoice == source.Invoice` AND `target.StockCode == source.StockCode`.
* **Actions:**
    * **When Matched:** `UPDATE SET *`
    * **When Not Matched:** `INSERT *`

---

## 📊 Phase 2: The Gold Layer (Business Aggregates)
**Context:** Star Schema & BI Optimization  
**Repo Path:** `project1_lakehouse/notebooks/03_model_gold.py`

### 1. Business Logic
* **Goal:** Create a "Daily Sales" Fact Table.
* **Aggregation:** Group by `Country` and `InvoiceDate`.
* **Metrics:**
    * `TotalRevenue`: Sum of (`Quantity * Price`)
    * `TotalOrders`: Count Distinct of `Invoice`

### 2. Performance Optimization
* **Technique:** **Z-Ordering**.
* **Action:** Run `OPTIMIZE gold_daily_sales ZORDER BY (InvoiceDate)`.
* **Why:** This co-locates data in the physical files, making filtering by date (a common BI pattern) massive faster via **Data Skipping**.

---

## 🛠️ Phase 3: Algorithmic Engineering (DSA)
**Context:** Graph Traversal & Queues  

### 3. Number of Islands (LeetCode #200)
* **Pattern:** Grid Traversal (BFS or DFS).
* **Engineering Relevance:** Used in clustering, image processing, and analyzing connected components in social graphs.

### 4. Implement Queue using Stacks (LeetCode #232)
* **Pattern:** Data Structure Design.
* **Logic:** Use two stacks (`input`, `output`) to reverse the LIFO nature of a stack into the FIFO nature of a queue.

---

## 🤖 Phase 4: GenAI "Hello Vector"
**Context:** Infrastructure Setup  

### 5. Vector Database Connectivity
* **Tool:** Pinecone (Cloud) or ChromaDB (Local).
* **Task:**
    1.  Initialize the client.
    2.  Create an index (Dimension: e.g., 1536 for OpenAI, 384 for MiniLM).
    3.  **Upsert** a dummy vector: `id="vec1", values=[0.1, 0.2...], metadata={"text": "test"}`.
    4.  **Query** it back to verify the pipeline.

---

## 📝 Deliverables & Verification

### Repository Sync
* **Location:** `data-engineering-portfolio-2026`
* **Checklist:**
    * [ ] `project1_lakehouse/notebooks/02_transform_silver.py` (Merge Logic).
    * [ ] `project1_lakehouse/notebooks/03_model_gold.py` (Aggregation + Z-Order).
    * [ ] `dsa/day7/` (C++ Solutions).
    * [ ] `docs/Week1/Day7/JOURNAL.md` (Logs & Verification).

### ✅ Verification Question
> *In the Silver Layer, if I receive a record with the same `InvoiceNo` but a different `Quantity` than what is currently in the table, what specific Delta command ensures the record is updated rather than duplicated?*

---