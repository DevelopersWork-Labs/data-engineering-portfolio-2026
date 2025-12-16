# 🚀 **Day 4: Skew Remediation & Vector Indexing**

**Phase:** Week 1 (Core Patterns & Internals)

**Focus:** Coding the "Salting" logic, Fixed-Size Sliding Windows, and Vector Database Internals.

**Time Allocation:** ~2 Hours (Weekday Sprint).

---

### **Phase 1: Algorithmic Engineering (DSA)**
**Context:** Fixed-Size Sliding Window | Time: ~45 Mins

**1. Permutation in String** (LeetCode #567)
* **Pattern:** **Fixed-Size Sliding Window**.
* **Logic:** Unlike the "Longest Substring" problem (Day 3) where the window size changed, here the window size is fixed to the length of string `s1`.
* **Task:** Check if `s2` contains a permutation of `s1`.
* **Hint:** Use two frequency arrays (or Hash Maps). Slide the window over `s2`, adding the new character and removing the old one. If `freq_array(window) == freq_array(s1)`, you found it.

**2. Max Consecutive Ones III** (LeetCode #1004) [Stretch / Highly Recommended]
* **Pattern:** Sliding Window with "Budget" ($K$ flips).
* **Logic:** Expand right. If you hit a zero, decrement $K$. If $K < 0$, shrink left.

---

### **Phase 2: Platform Architecture (Applied Coding)**
**Context:** PySpark Implementation | Time: ~45 Mins

**3. Implementing the "Salted Join"**
* **Goal:** You know the *theory* of Salting (Day 1/2). Now write the **production code**.
* **Scenario:** You have a skewed DataFrame `df_large` and a small DataFrame `df_small`. You need to join them on `user_id`.
* **Task:** Write a Python/PySpark function snippet (in your local editor) that performs these steps:
    1.  **Salt the Large Table:** Add a new column `salt` with a random integer (0 to $N$).
    2.  **Explode the Small Table:** Duplicate every row in the small table $N$ times (one for each salt value).
    3.  **Join:** Join on `user_id` AND `salt`.
* **Deliverable:** A code snippet in `Week1/Day4/salted_join.py`. (You don't need to execute it if you don't have a cluster, just write the correct syntax).

---

### **Phase 3: GenAI Architecture (Vector Stores)**
**Context:** Theory & Indexing | Time: ~30 Mins

**4. The Vector Database & HNSW**
* **Topic:** **Approximate Nearest Neighbor (ANN)** search.
* **Problem:** If you have 1 Million embeddings, calculating Cosine Similarity against *all* of them (Brute Force) is too slow ($O(N)$).
* **Solution:** **HNSW (Hierarchical Navigable Small World)**.
* **Research:** How does HNSW allow us to find similar vectors in $O(\log N)$ time? (Think of it like a "Skip List" for graphs).
* **Deliverable:** A simple analogy for HNSW in your notes.

---

### **Phase 4: Portfolio Sync**
**Context:** Personal Device | Time: ~15 Mins

**5. Repository Synchronization**
* **Repo:** `data-engineering-portfolio-2026`
* **Action:**
    * Commit `DSA/Day4/` solutions.
    * Commit `Week1/Day4/salted_join.py` (Your Salting function).
    * Update `Week1/Day4/JOURNAL.md` with your HNSW analogy.

---

### 🛡️ **Mentor Check-In (Unlock Day 5)**

To clear Day 4, submit:

1.  **[GitHub Link]** Your `salted_join.py` file. (I want to see the `explode` logic).
2.  **[The Answer]** Verification Question: *In a Vector DB, if I use an "Inverted File Index" (IVF), I partition the vector space into clusters. When a query comes in, do I search ALL clusters or just the closest ones?*

**Code the solution.**