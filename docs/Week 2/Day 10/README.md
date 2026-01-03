# 🚀 Day 10: The Streaming Lakehouse (Project 2 Kickoff)

**Phase:** Week 2 Weekend (The Build)  
**Focus:** Real-Time Data Pipelines, Spark Structured Streaming, Auto Loader, and BST Algorithms.  
**Estimated Time:** 4-5 Hours (Deep Work Workshop)  

---

## 🎯 Objectives
1.  **Engineering Implementation:** Pivot from Batch processing to **Structured Streaming**. Build the ingestion layer for **Project 2** using Databricks Auto Loader (`cloudFiles`).
2.  **Architecture:** Master the mechanism of **Checkpointing** and how Spark ensures **Exactly-Once** processing semantics in streaming.
3.  **Algorithmic Proficiency:** Master **Binary Search Trees (BST)**, a fundamental structure for efficient lookup and range queries ($O(\log N)$).
4.  **GenAI Preparation:** Implement **Text Chunking** with overlap, a critical preprocessing step for high-quality RAG retrievals.

---

## 🏗️ Phase 1: Project 2 — Streaming Ingestion
**Context:** "Retail360" Real-Time Layer  
**Repo Path:** `project2_streaming/notebooks/04_stream_bronze.py`

### 1. The Stream Source (Auto Loader)
* **Goal:** Ingest files immediately as they land in the source directory (`dbfs:/FileStore/raw/retail/`).
* **Technology:** Use `spark.readStream.format("cloudFiles")`.
* **Critical Configuration:**
    * **Format:** `.option("cloudFiles.format", "csv")`
    * **Checkpointing:** You **MUST** define a `checkpointLocation`. This is the "bookmark" that tracks processed files.
    * **Trigger:** Use `.trigger(availableNow=True)` to process all currently available data and then stop (Cost-Optimized Batch Mode).

### 2. Schema Evolution
* **Experiment:**
    1.  Run the stream once.
    2.  Add a new column to a dummy CSV file and upload it.
    3.  Run the stream again.
* **Task:** Configure `.option("cloudFiles.schemaLocation", ...)` to ensure the stream detects the new column and merges it into the Delta table automatically without failing.

---

## 🛠️ Phase 2: Algorithmic Engineering (DSA)
**Context:** Binary Search Trees (BST)  

### 3. Validate Binary Search Tree (LeetCode #98)
* **Pattern:** Recursion with Range.
* **Logic:** A node is valid only if: `min_val < node.val < max_val`.
* **Recursion:** Pass updated ranges down:
    * Left Child: `(min, current.val)`
    * Right Child: `(current.val, max)`

### 4. Lowest Common Ancestor of a BST (LeetCode #235)
* **Pattern:** BST Property Navigation.
* **Logic:**
    * If `p` and `q` are both smaller than `root`, go **Left**.
    * If `p` and `q` are both larger than `root`, go **Right**.
    * Otherwise, the current `root` is the split point (LCA).

### 5. Kth Smallest Element in a BST (LeetCode #230)
* **Pattern:** In-Order Traversal.
* **Logic:** In-order traversal (Left → Root → Right) visits BST nodes in sorted ascending order. Stop at the $k$-th visited node.

---

## 🤖 Phase 3: GenAI RAG Prep
**Context:** Text Pre-processing  

### 6. Text Chunking Strategy
* **Task:** Write a Python function `chunk_text(text, chunk_size=500, overlap=50)`.
* **Why Overlap?** To preserve semantic context at the boundaries. If a sentence is cut in half, the overlap ensures the next chunk contains the full thought.
* **Deliverable:** A local script testing this function on a sample Wikipedia paragraph.

---

## 📝 Deliverables & Verification

### Repository Sync
* **Location:** `data-engineering-portfolio-2026`
* **Checklist:**
    * [ ] `project2_streaming/notebooks/04_stream_bronze.py` (Streaming Logic).
    * [ ] `dsa/day10/` (BST Solutions).
    * [ ] `docs/Week2/Day10/JOURNAL.md`.

### Journal Reflection
* **Streaming:** Explain strictly **why** deleting the `checkpoint` directory causes Spark to re-process all files from scratch.
* **GenAI:** Explain how chunk overlap improves Retrieval (RAG) accuracy.

### ✅ Verification Question
> *If I delete the `checkpoint` directory of a running streaming job, what happens when I restart the job?*

---