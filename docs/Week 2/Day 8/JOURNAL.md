# 📘 Week 1 — Day 7 Journal  

**Date:** 02/01/2026

----
## 🛠️ Phase 1: Algorithmic Engineering (DSA)

### 1. Binary Search (LeetCode #704)
Implemented a binary search algorithm to locate a target value in a sorted array.

Initialized left and right pointers to define the search boundaries.  
Repeatedly calculated the middle index and compared the middle element with the target.  
Narrowed the search space by adjusting pointers based on comparison results.  
Returned the index of the target when found, or `-1` when the target was not present.

### 2. Search a 2D Matrix (LeetCode #74)
Implemented a binary search approach on a 2D matrix by treating it as a virtual 1D sorted array.

Calculated the effective search range using the total number of elements in the matrix.  
Mapped the computed mid index to 2D coordinates using row and column calculations.  
Applied binary search logic to locate the target value within the matrix.  
Returned a boolean result indicating whether the target exists in the matrix.

----
## 🏗️ Phase 2: Engineering Orchestration

Created a Databricks Job named `retail360_daily_pipeline` to automate the execution of the Lakehouse pipeline using a task-based workflow.

Configured the job with three dependent tasks:
- **Bronze Task:** Executes the `01_ingest_bronze` notebook to ingest raw data.
- **Silver Task:** Executes the `02_transform_silver` notebook and is configured to run after the Bronze task.
- **Gold Task:** Executes the `03_model_gold` notebook and is configured to run after the Silver task.

Defined task dependencies to enforce the execution order: Bronze → Silver → Gold.

Executed the job manually using the “Run Now” option and observed a successful run:
- All three tasks completed successfully.
- Each task ran sequentially based on the configured dependencies.
- The workflow execution completed without errors.

Verified the pipeline execution using the job run graph view, confirming correct orchestration of the end-to-end Lakehouse process.
![alt text](image.png)

----
## 📐 Phase 3: System Design

----
## Verification Question

**Question:**  
*In a Binary Search on a sorted array of size 1,000,000, what is the **maximum** number of comparisons needed to find an element? (Approximate is fine).*

**Answer:**  
- in binary search, the amount of comparisons is O(log n)
- so every iterations amount of comparisions to be done will get halfed. 1m->500k->250k->125k->62k->31k->15k->7k->3k->1k->500->250->125->62->31->15->7->3->1
- so the maximum number of comparisons needed to find an element is 20

----

# ✔️ Day 8 Status: _IN-PROGRESS_
