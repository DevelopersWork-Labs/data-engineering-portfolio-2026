# 🚀 Day 9: Data Quality & Expectations

**Phase:** Week 2 (Automation & Quality)  
**Focus:** Data Quality (DQ) Frameworks, Assertions, and Tree Algorithms.  
**Estimated Time:** 2 Hours (Weekday Sprint)  

---

## 🎯 Objectives
1.  **Engineering Reliability:** Move beyond "running pipelines" to "reliable pipelines." Implement **Data Quality Gates** that prevent bad data from corrupting your Silver/Gold tables.
2.  **Algorithmic Proficiency:** Master **Tree Traversal (DFS/BFS)**. Trees are the underlying data structure for file systems, JSON/XML parsing, and query execution plans.
3.  **System Design:** Understand the **Write-Audit-Publish (WAP)** pattern, the industry standard for ensuring data consistency in Data Lakes.

---

## 🛠️ Phase 1: Algorithmic Engineering (DSA)
**Context:** Recursion & Hierarchies | Time: ~45 Mins

### 1. Maximum Depth of Binary Tree (LeetCode #104)
* **Pattern:** Depth-First Search (DFS).
* **Logic:** The depth of a tree is `1 + max(depth(left), depth(right))`. This is the purest form of recursion.

### 2. Invert Binary Tree (LeetCode #226)
* **Pattern:** DFS / Mirroring.
* **Logic:** Swap the left and right children, then recursively invert the subtrees.
* **Relevance:** Famous for being a standard interview filter question.

### 3. Same Tree (LeetCode #100)
* **Pattern:** Structural Comparison.
* **Logic:** Two trees are the same if:
    1.  Both nodes are `null` (True).
    2.  One is `null` but the other isn't (False).
    3.  Values match AND `left` subtrees are the same AND `right` subtrees are the same.

---

## 🏗️ Phase 2: Engineering Data Quality
**Context:** "Retail360" Silver Layer | Time: ~45 Mins

### 4. Implement Data Quality Gates
* **Goal:** Prevent invalid data (e.g., negative `Quantity`) from entering the Silver Layer.
* **Task:** Modify `notebooks/02_transform_silver` to include an assertion step *before* the MERGE operation.
* **Implementation:**
    ```python
    # Example Logic
    bad_records = df.filter("Quantity < 0 OR Invoice IS NULL")
    if bad_records.count() > 0:
        raise Exception(f"DQ FAILED: Found {bad_records.count()} invalid records.")
    ```
* **Test:** Manually insert a bad record into Bronze and verify that the Silver job **fails** instead of processing garbage.

---

## 📐 Phase 3: System Design
**Context:** Architectural Consistency | Time: ~30 Mins

### 5. The WAP Pattern (Write-Audit-Publish)
* **Topic:** Preventing "Dirty Reads."
* **Research:** How does Netflix/Uber ensure that a user never sees a dashboard update "halfway"?
* **Mechanism:**
    1.  **Write:** Write data to a hidden/staging partition or table.
    2.  **Audit:** Run DQ checks (like the one you just wrote).
    3.  **Publish:** If Checks Pass → Swap the pointer (or commit the transaction) to make data live. If Checks Fail → Delete the staged data.

---

## 📝 Deliverables & Verification

### Repository Sync
* **Location:** `data-engineering-portfolio-2026`
* **Checklist:**
    * [ ] `dsa/day9/` (Tree Solutions).
    * [ ] `project1_lakehouse/notebooks/02_transform_silver.py` (Updated with Exception logic).
    * [ ] `docs/Week2/Day9/JOURNAL.md` (WAP Pattern explanation).

### ✅ Verification Question
> *If I have a binary tree with $N$ nodes, what is the Time Complexity of visiting every node exactly once?*

---