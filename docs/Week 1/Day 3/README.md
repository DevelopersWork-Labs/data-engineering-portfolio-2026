### 🚀 **Day 3 Task Card: Windows & Partitioning**

**Phase:** Week 1 (Core Patterns & Internals)

**Focus:** Sliding Window Pattern, Partitioning Strategy, and Vector Embeddings.

**Context:** Weekday Mode (Office Execution / Home Sync).

---

### **Phase 1: Algorithmic Engineering (DSA)**
**Context:** Office Breaks / LeetCode | Time: ~45 Mins

**1. Sliding Window Pattern**
* **Objective:** Master the "Window" technique to avoid nested loops ($O(N^2)$ → $O(N)$).
* **Task:** Solve 2 Mandatory Problems.
    1.  **Best Time to Buy and Sell Stock** (LeetCode #121)
        * *Concept:* Dynamic Window (Tracking Min Price).
        * *Why:* Foundational for time-series analysis in data pipelines.
    2.  **Longest Substring Without Repeating Characters** (LeetCode #3)
        * *Concept:* Variable Size Sliding Window + Hash Set.
        * *Why:* This simulates stream processing logic (deduplication over a time window).

---

### **Phase 2: Platform Architecture (Databricks Optimization)**
**Context:** Office Learning | Time: ~45 Mins

**2. Partitioning vs. Z-Ordering**
* **Topic:** **Domain 3: Performance Optimization**.
* **Research Task:** Compare "Partitioning" vs. "Z-Order Clustering."
* **Guiding Questions for Notes:**
    * **Partitioning:** Good for low cardinality (e.g., `Date`, `Country`). Why is it bad for high cardinality columns like `UserID`? (Hint: "Small File Problem").
    * **Z-Ordering:** How does it co-locate related data in the same set of files *without* creating sub-directories?
* **Deliverable:** A simple "When to use what" decision rule.

---

### **Phase 3: GenAI Concepts (Embeddings)**
**Context:** Conceptual | Time: ~30 Mins

**3. Vector Embeddings (Text to Numbers)**
* **Topic:** **The Engine of RAG**.
* **Concept:** You saw "Tokens" yesterday. Today, understand "Vectors."
* **Action:** Read about **Cosine Similarity**.
* **Thought Experiment:**
    * If "King" is vector `[0.9, 0.1]` and "Queen" is `[0.85, 0.15]`, they are close in space.
    * Why is `Cosine Distance` used instead of `Euclidean Distance` in high-dimensional spaces?
* **Output:** 1-sentence definition of *Embeddings* in your journal.

---

### **Phase 4: Portfolio Sync**
**Context:** Personal Device | Time: ~15 Mins

**4. Repository Synchronization**
* **Repo:** `data-engineering-portfolio-2026`
* **Action:**
    * Commit `DSA/Day3/` solutions.
    * Update `Week1/Day3/JOURNAL.md` with:
        * **Optimization:** Your rule for Partitioning vs. Z-Ordering.
        * **GenAI:** Definition of Embeddings.

---

### 🛡️ **Mentor Check-In (Unlock Day 4)**

To clear Day 3, submit:

1.  **[GitHub Link]** Your `JOURNAL.md`.
2.  **[The Answer]** Verification Question: *If I have a 1TB table and I partition it by `Second` (timestamp), what specific performance issue will I create in the file system?*
