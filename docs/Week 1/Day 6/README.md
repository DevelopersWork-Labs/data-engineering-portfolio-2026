# 🚀 Day 6: Project 1 Kickoff — The Retail360 Lakehouse

**Phase:** Week 1 Weekend (The Build)  
**Focus:** Bronze Layer Ingestion (Code), Schema Evolution, and Stack Algorithms.  
**Type:** 5-Hour Workshop (Deep Work)  

---

## 🎯 Workshop Objectives
1.  **System Implementation:** Move from Databricks "Labs" to a persistent **Project Repository**. Build the **Bronze Layer** of the "Retail360" Lakehouse.
2.  **Engineering Patterns:** Implement **Schema Evolution** and **Audit Columns**—features that distinguish a "Student Project" from a "Production Pipeline."
3.  **Algorithmic Mastery:** Master **Stack (LIFO)** data structures, which are essential for parsing and backtracking interview questions.

---

## 🏗️ Phase 1: Project 1 Implementation (Bronze Layer)

**Context:** You are building the data platform for a global retailer.
**Repo Path:** `project1_lakehouse/notebooks/01_ingest_bronze.py`

### 1. Dataset & Storage Setup
* **Action:** Download the **"Online Retail II"** dataset (Kaggle) or generate synthetic data (Customers, Orders) using `faker`.
* **Storage:** Upload raw CSVs to `dbfs:/FileStore/raw/retail/`.
    * *Note:* In a real job, this would be S3/ADLS mounted to DBFS.

### 2. The Ingestion Logic (Production Grade)
* **Requirement:** Write a generic function `ingest_raw_to_bronze(source_path, table_name)`.
* **Critical Features to Code:**
    1.  **Format:** Read `CSV` -> Write `DELTA`.
    2.  **Audit Columns:** You **MUST** append:
        * `_ingest_timestamp`: `current_timestamp()`
        * `_source_file`: `input_file_name()`
    3.  **Schema Handling:** Set `.option("mergeSchema", "true")`.
        * *Why?* Bronze must never fail if the client adds a new column. It should just ingest it.
    4.  **Partitioning:** Do **NOT** partition Bronze tables (usually too many small files).

**Deliverable:** A successful run where you ingest data, then upload a *new* CSV with an extra column, run it again, and confirm the table evolved.

---

## 🛠️ Phase 2: DSA Workshop (Stacks)

**Focus:** LIFO (Last-In, First-Out) Patterns.

### 3. Valid Parentheses (LeetCode #20)
* **Concept:** Matching Pairs.
* **Logic:** Use a stack. Push `(`, pop when `)`. If stack is empty at the end, valid.

### 4. Min Stack (LeetCode #155)
* **Concept:** Class Design & Optimization.
* **Challenge:** `getMin()` must be $O(1)$.
* **Trick:** Maintain a second stack that only pushes the *current minimum* value.

### 5. Evaluate Reverse Polish Notation (LeetCode #150)
* **Concept:** Postfix Evaluation.
* **Relevance:** This is exactly how Spark's Catalyst Optimizer parses your SQL expressions tree.

---

## 🤖 Phase 3: GenAI Infrastructure Prep

### 6. Vector Database Setup
* **Goal:** Prepare for Project 3 (RAG).
* **Action:**
    1.  Sign up for **Pinecone** (Free Tier) OR set up **ChromaDB** locally.
    2.  Get your **API Key**.
    3.  **Security:** Create a `.env` file or use Databricks Secrets to store it. *Never push keys to GitHub.*

---

## 📝 Deliverables & Verification

### Repository Sync
* **Path:** `data-engineering-portfolio-2026`
    * [ ] `project1_lakehouse/notebooks/01_ingest_bronze.py` (The Code).
    * [ ] `dsa/day6/` (Stack Solutions).
    * [ ] `docs/Week1/Day6/JOURNAL.md`.

### Journal Reflection
* **Architecture:** Sketch the schema of your `orders_bronze` table (including audit columns).
* **Engineering:** Explain *why* we use `mergeSchema` in Bronze but `enforceSchema` in Silver.

### ✅ Verification Question
> *If I process a CSV file today with 5 columns, and tomorrow I receive a CSV with 6 columns, what happens to my Bronze Delta Table if `mergeSchema` is set to `false`?*

---