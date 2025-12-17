# 📘 Week 1 — Day 5 Journal  

**Date:** 18/12/2025

----

## Phase 1 — Algorithmic Engineering (DSA)

### 1.1. Reverse Linked List (#206)
Implemented an iterative approach to reverse a singly linked list.

Traversed the list using a pointer while maintaining references to the previous, current, and next nodes.  
Updated the `next` pointer of each node to reverse the direction of the list.  
Returned the new head of the reversed linked list after completing the traversal.

### 1.2. Merge Two Sorted Lists (#21)
Implemented an iterative solution to merge two sorted singly linked lists.

Compared node values from both lists and appended the smaller node to the merged list.  
Advanced pointers accordingly while maintaining sorted order.  
After one list was exhausted, appended the remaining nodes from the other list to complete the merged result.

----

## Phase 2 — Distributed Architecture

### 2.3. CAP Theorem & Eventual Consistency
Reviewed the CAP theorem and its implications in distributed systems.

- **Consistency:** Ensures that all nodes in a distributed system return the same, most recent data.
- **Availability:** Guarantees that every request receives a response, regardless of node state.
- **Partition Tolerance:** Ensures the system continues to operate despite network partitions.

Noted that partition tolerance is non-negotiable in distributed systems, leaving a trade-off between consistency and availability.

Studied how Amazon S3 operates as an **AP system** at the storage level.  
Observed that layering **Delta Lake** on top of object storage introduces transactional guarantees, effectively enforcing **CP behavior** by maintaining a transaction history through the `_delta_log`.

---

## Phase 3 — GenAI Architecture

### 3.4. The 5-Step RAG Pipeline
Reviewed the Retrieval-Augmented Generation (RAG) workflow and its core stages:

**Workflow:** _Ingestion → Chunking → Embedding → Retrieval → Generation_

- **Ingestion:** Collecting data from sources such as PDFs, HTML pages, and databases.
- **Chunking:** Splitting large documents into smaller, context-preserving segments.
- **Embedding:** Converting text chunks into vector representations.
- **Retrieval:** Performing similarity search using ANN techniques to find relevant context vectors.
- **Generation:** Supplying the retrieved context along with the user query to an LLM to generate responses.

---

## Verification Question

**Question:**  
*If you merge two sorted linked lists of size 1 million each, how many comparisons will the algorithm perform in the absolute worst-case scenario?*

**Answer:**  
- **Best Case:** 1,000,000 comparisons, when all elements of one list are either smaller or larger than the other.
- **Worst Case:** 1,999,999 comparisons, when elements from both lists are perfectly interleaved.

----

# ✔️ Day 5 Status: _CLEARED_