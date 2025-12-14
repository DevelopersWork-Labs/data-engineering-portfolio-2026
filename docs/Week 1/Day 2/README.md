# 🚀 **Day 2: The Lakehouse Foundation**

**Phase:** Week 1 (Core Patterns & Internals)

**Focus:** Delta Lake Internals, Indexing Strategies, and Associate Certification Refresh.

**Time Allocation:** ~5 Hours (Weekend Workshop Mode).

---

### **Phase 1: Algorithmic Engineering (DSA)**
**Context:** Deep Work | Time: ~1.5 Hours

**1. Optimization with Hash Maps & Heaps**
* **Objective:** Master "Pre-computation" and "Heaps." These are the algorithms behind database query optimization.
* **Task:** Solve 3 Mandatory Problems (LeetCode).
    1.  **Two Sum** (#1)
        * *Concept:* Hash Lookups ($Target - Current$). This mimics Hash Joins.
    2.  **Top K Frequent Elements** (#347)
        * *Constraint:* Solve using a **Min-Heap** or **Bucket Sort** ($O(N)$ or $O(N \log K)$). Do NOT use global sort ($O(N \log N)$).
        * *Why:* In Big Data, finding "Top N" items shouldn't require sorting the whole petabyte.
    3.  **Product of Array Except Self** (#238) [Critical]
        * *Constraint:* $O(N)$ Time, $O(1)$ Space, **No Division**.
        * *Why:* This teaches "Prefix Arrays" (cumulative aggregations), a key technique in window functions.
* **Deliverable:** Optimized code files in `DSA/` folder.

---

### **Phase 2: Platform Architecture (Databricks Associate)**
**Context:** Hands-on Lab | Time: ~2.0 Hours

**2. The Delta Log (ACID Transactions)**
* **Topic:** **Domain 2: ELT with Spark SQL and Python**.
* **Lab Action:**
    1.  Create a Delta Table: `CREATE TABLE events (id INT, data STRING) USING DELTA;`
    2.  Perform 2-3 `INSERT` operations.
    3.  **Inspect File System:** `%fs ls dbfs:/user/hive/warehouse/events/_delta_log/`
    4.  **Analysis:** Locate the `.json` files (commits).
* **Key Insight to Log:** How does the presence of these JSON files enable **Time Travel** on a generic file system like S3?

**3. Medallion Architecture**
* **Topic:** **Standard Design Patterns**.
* **Task:** Define the *strict* purpose of each layer in your notes:
    * **Bronze:** Raw, immutable, append-only.
    * **Silver:** Cleaned, deduplicated, enriched (The "Source of Truth").
    * **Gold:** Aggregated, business-level metrics (Ready for BI).

---

### **Phase 3: System Internals (Storage Design)**
**Context:** Theory & Research | Time: ~1.0 Hour

**4. Parquet Internals & Data Skipping**
* **Topic:** **File Layout & Statistics**.
* **Research:** How "Min/Max Statistics" in the file footer enable performance.
* **Scenario:** If a file has `ID_Min=100`, `ID_Max=200`:
    * Query: `SELECT * FROM table WHERE ID=50`.
    * **Mechanism:** Explain *why* the engine skips this file entirely without reading a single row (Data Skipping).

---

### **Phase 4: GenAI & Portfolio Sync**
**Context:** Experimentation & Documentation | Time: ~0.5 Hours

**5. GenAI Lab: Tokenization**
* **Topic:** **LLM Input Processing**.
* **Action:** Use a Tokenizer tool (Tiktokenizer or Python `tiktoken`).
* **Experiment:** Compare the token count of a standard word (e.g., "Data") vs. a long number (e.g., "794625452451").
* **Insight:** Understand why numerical data consumes more context window than text.

**6. Repository Synchronization**
* **Repo:** `data-engineering-portfolio-2026`
* **Action:**
    * Commit `DSA/` solutions.
    * Update `Week1/Day2/JOURNAL.md` with:
        * **Delta Log:** A snippet of the JSON commit log.
        * **System Design:** Your explanation of Data Skipping.
        * **GenAI:** Tokenizer experiment results.

---

### 🛡️ **Mentor Check-In (Unlock Day 3)**

To clear Day 2, please submit:

1.  **[GitHub Link]** Your `JOURNAL.md` containing the Delta Log analysis and Data Skipping explanation.
2.  **[The Answer]** Verification Question: *If I Perform 10 separate `INSERT` operations on a Delta Table, how many JSON files will typically be created in the `_delta_log` folder?*