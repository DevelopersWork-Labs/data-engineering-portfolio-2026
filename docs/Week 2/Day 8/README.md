# 🚀 Day 8: Orchestration & Binary Search

**Phase:** Week 2 (Automation & Quality)  
**Focus:** Databricks Workflows (Jobs), Multi-Task DAGs, and Binary Search Algorithms.  
**Estimated Time:** 2 Hours (Weekday Sprint)  

---

## 🎯 Objectives
1.  **Engineering Automation:** Transition from manual notebook execution to automated **Databricks Workflows**. Build a dependent pipeline (DAG) for the "Retail360" Lakehouse.
2.  **Algorithmic Proficiency:** Master **Binary Search**, the fundamental algorithm for efficient $O(\log N)$ searching in sorted datasets.
3.  **System Design:** Understand **Directed Acyclic Graphs (DAGs)** and their role in modern data orchestration (Airflow, Databricks Jobs) versus traditional CRON scheduling.

---

## 🛠️ Phase 1: Algorithmic Engineering (DSA)
**Context:** Divide and Conquer | Time: ~45 Mins

### 1. Binary Search (LeetCode #704)
* **Pattern:** Standard Binary Search.
* **Logic:** Repeatedly divide the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half.
* **Key Detail:** Handle `mid` calculation carefully to avoid integer overflow: `mid = left + (right - left) / 2`.

### 2. Search a 2D Matrix (LeetCode #74)
* **Pattern:** Virtual Flattening.
* **Logic:** Treat the 2D matrix ($m \times n$) as a sorted 1D array of size $m \times n$.
* **Mapping:** Convert a 1D index `idx` to 2D coordinates:
    * `row = idx / n`
    * `col = idx % n`
* **Constraint:** Achieve $O(\log(m \cdot n))$ complexity.

---

## 🏗️ Phase 2: Engineering Orchestration
**Context:** The "Retail360" Pipeline | Time: ~45 Mins

### 3. Create a Databricks Job (DAG)
* **Goal:** Automate the execution of your Lakehouse notebooks in the correct order.
* **Task:** Create a new Job named `retail360_daily_pipeline`.
    * **Task 1 (Bronze):** Select `notebooks/01_ingest_bronze`.
    * **Task 2 (Silver):** Select `notebooks/02_transform_silver`. **Dependency:** Task 1.
    * **Task 3 (Gold):** Select `notebooks/03_model_gold`. **Dependency:** Task 2.
* **Execution:** Run the job manually ("Run Now") and verify that all 3 tasks turn green.

---

## 📐 Phase 3: System Design
**Context:** Orchestration Patterns | Time: ~30 Mins

### 4. DAGs vs. CRON
* **Research:** Why do data teams prefer DAG-based orchestrators (Airflow, Prefect, Databricks Workflows) over simple CRON scripts?
* **Key Concept:** **Backfilling**.
    * *Scenario:* The pipeline fails on Tuesday. We fix the bug on Wednesday.
    * *Question:* How does a DAG allow us to safely re-run *only* Tuesday's data processing without duplicating Wednesday's data?

---

## 📝 Deliverables & Verification

### Repository Sync
* **Location:** `data-engineering-portfolio-2026`
* **Checklist:**
    * [ ] `dsa/day8/` (Binary Search Solutions).
    * [ ] `docs/assets/week2_dag.png` (Screenshot of your Databricks Job Run Graph).
    * [ ] `docs/Week2/Day8/JOURNAL.md`.

### ✅ Verification Question
> *In a Binary Search on a sorted array of size 1,000,000, what is the **maximum** number of comparisons needed to find an element? (Approximate is fine).*

---