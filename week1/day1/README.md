# 🚀 **Day 1: Foundations & Architecture**

**Phase:** Week 1 (Core Patterns & Internals)
**Focus:** Algorithmic Warm-up, Distributed Storage Internals, and Local AI Setup.
**Context:** Professional Execution (Workstation) & Portfolio Sync (Personal Device).

---

### **1. Objectives**
* **Algorithmic Proficiency:** Re-establish muscle memory for **Hash Maps** and **Frequency Counters**, the foundational building blocks for distributed shuffling.
* **Data Engineering Internals:** Master **Data Skew** and **Salting** (Databricks DE Professional Domain 3.0).
* **System Design:** Understand the fundamental storage trade-offs (Row-oriented vs. Column-oriented) used in modern Lakehouses.
* **GenAI Engineering:** Verify local inference capabilities.

---

### **2. DSA Challenge: Arrays & Hashing**
**Goal:** Solve 3 Mandatory problems. Attempt 2 Optional if time permits.

#### **Mandatory (The Core 3)**
1.  **Contains Duplicate** (LeetCode #217)
    * *Focus:* Efficient lookups ($O(1)$) vs. scanning ($O(N)$).
2.  **Valid Anagram** (LeetCode #242)
    * *Focus:* Frequency counting. This mimics how Spark counts terms in a dataset.
3.  **Group Anagrams** (LeetCode #49)
    * *Focus:* Key generation strategies. This simulates the logic behind a **Shuffle/GroupBy** operation in Spark.

#### **Optional (Stretch)**
4.  **Two Sum** (LeetCode #1)
    * *Focus:* Complement lookups.
5.  **Top K Frequent Elements** (LeetCode #347)
    * *Focus:* Heaps or Bucket Sort (Optimization).

---

### **3. Certification Track: Databricks DE Professional**
* **Module:** Performance Optimization (Partitioning & Shuffle).
* **Resource:** Databricks Partner Academy / Documentation.
* **Task:** Complete the module on **Data Skew**.
* **Key Concepts to Log:**
    * **Identification:** How to spot skew in the Spark UI (straggler tasks).
    * **Mitigation:** The specific mechanics of **Salting** (adding randomness to high-cardinality keys).

---

### **4. System Design Primer**
* **Topic:** **Row-Oriented vs. Column-Oriented Storage**.
* **Task:** Research and document the core difference.
* **Guiding Questions for Notes:**
    * Why is **Parquet** (Columnar) superior for analytical queries (OLAP) like `SUM` or `AVG`?
    * Why is **Postgres** (Row-based) superior for transactional updates (OLTP)?

---

### **5. GenAI Lab (Local Environment)**
* **Task:** Verify local LLM function.
* **Action:**
    1.  Pull model: `ollama pull llama3` (or `mistral`).
    2.  Execute a test prompt via Python or CLI: *"Explain 'Vector Embeddings' to a data engineer in 2 sentences."*
* **Outcome:** Confirm text generation works without external API calls.

---

### **6. Portfolio Sync (Personal Device)**
* **Repository:** `data-engineering-portfolio-2026`
* **Action:**
    1.  **DSA:** Update `DSA/` with your solutions (re-typed or pasted).
    2.  **Journal:** Update `Week1/Day1/JOURNAL.md` with:
        * **DSA Log:** A brief note on the "Signature" logic used for Group Anagrams.
        * **Certification Log:** 3 bullet points defining *Data Skew*.
        * **System Design:** A 1-sentence summary of when to use Columnar storage.
        * **GenAI Log:** The definition of "Vector Embeddings" provided by your local model.

---

### 🛡️ **Mentor Check-In (Unlock Day 2)**

To clear Day 1, please submit:

1.  **[GitHub Link]** Your `JOURNAL.md` containing the summary of today's work.
2.  **[The Answer]** In your reply, answer this verification question: *In a Salted Join, if you salt the skew key with a range of 1-5, by what factor does the size of the skewed partition theoretically decrease?*
