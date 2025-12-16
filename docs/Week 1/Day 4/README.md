# 🚀 Day 5: Pointers & Distributed Consistency

**Phase:** Week 1 (Core Patterns & Internals)  
**Focus:** Linked List Memory Management, CAP Theorem, and RAG Architecture.  
**Estimated Time:** 2.0 Hours  

---

## 🎯 Objectives
1.  **Algorithmic Proficiency:** Master pointer manipulation and iterative merging logic, the foundational operations for query engines (Sort-Merge Joins) and file systems.
2.  **System Design:** Analyze trade-offs in distributed data systems using the **CAP Theorem** (Consistency vs. Availability).
3.  **GenAI Architecture:** Deconstruct the standard **RAG (Retrieval-Augmented Generation)** pipeline into its 5 core components.

---

## 🛠️ Phase 1: Algorithmic Engineering (DSA)
**Context:** Pointers & Memory Management  

### 1. Reverse Linked List (LeetCode #206)
* **Pattern:** Two Pointers (Iterative).
* **Engineering Relevance:** Manipulating pointers (`next`, `prev`) mimics how databases link data pages and how distributed logs chain commits.
* **Constraint:** Solve in $O(N)$ Time and $O(1)$ Space.

### 2. Merge Two Sorted Lists (LeetCode #21)
* **Pattern:** Merge Step.
* **Engineering Relevance:** This algorithm is the engine behind **Sort-Merge Joins** in Spark and SQL. Understanding this logic is key to optimizing large-scale shuffles.
* **Logic:** Compare heads of $L1$ and $L2$, attach the smaller node to the result, and advance the pointer.

---

## 🏗️ Phase 2: Distributed Architecture
**Context:** System Design & Trade-offs  

### 3. The CAP Theorem & Eventual Consistency
* **Topic:** Distributed System Constraints.
* **Research Task:** Analyze the **CAP Theorem** (Consistency, Availability, Partition Tolerance).
    * **CP Systems:** (e.g., HBase, traditional RDBMS) Prioritize consistency; system may become unavailable during network partitions.
    * **AP Systems:** (e.g., Cassandra, DNS) Prioritize availability; system accepts writes during partitions but risks "stale" reads.
* **Critical Analysis:**
    * **Scenario:** Is **Delta Lake on S3** a CP or AP system? S3 is eventually consistent (AP), but Delta adds a transaction log. How does this shift the classification?

---

## 🤖 Phase 3: GenAI Architecture
**Context:** RAG Pipeline Design  

### 4. The 5-Step RAG Pipeline
* **Topic:** Retrieval-Augmented Generation.
* **Task:** Define the standard workflow for Project 3.
* **Components:**
    1.  **Ingestion:** Extracting text from raw sources (PDFs, HTML).
    2.  **Chunking:** Splitting text into context-aware segments (handling overlap).
    3.  **Embedding:** Converting chunks into dense vector representations.
    4.  **Retrieval:** Performing Vector Similarity Search (ANN) to find Top-K context.
    5.  **Generation:** Injecting context + query into the LLM context window for the final answer.

---

## 📝 Phase 4: Portfolio & Deliverables

### Repository Synchronization
* **Location:** `data-engineering-portfolio-2026`
* **Actions:**
    * [ ] Commit optimized C++ solutions for **#206** and **#21** to `dsa/day5/`.
    * [ ] Update `docs/Week1/Day5/JOURNAL.md` with:
        * **CAP Analysis:** Classification of Delta Lake (Acid vs. Eventual Consistency).
        * **RAG Definitions:** Brief 1-sentence architectural definitions for the 5 steps.

### ✅ Verification Question
> *If you merge two sorted linked lists of size 1 Million each, how many comparisons will the algorithm perform in the absolute worst-case scenario?*

---