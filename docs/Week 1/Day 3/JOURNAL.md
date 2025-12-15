# 📘 Week 1 — Day 3 Journal  

**Date:** 16/12/2025

----

## Phase 1 — Algorithmic Engineering (DSA)

### 1.1. Longest Substring Without Repeating Characters (#3)
Solved using the sliding window technique with two pointers.  
Maintained a window of unique characters using a fixed-size frequency array.  
Expanded the window by moving the right pointer and shrank it from the left when a duplicate character was encountered.  
Tracked and updated the maximum window length during iteration.

### 1.2. Best Time to Buy and Sell Stock (#121)
Implemented two approaches to compute the maximum profit from a single buy-sell transaction.

- First approach explored comparing prices across future days relative to a chosen buy day.
- Second approach used a single-pass strategy by tracking the minimum price seen so far and computing profit against the current price.

Validated results across increasing, decreasing, and fluctuating price sequences.

----

## Phase 2 — Platform Architecture (Databricks Optimization)

### 2.2. Partitioning vs. Z-Ordering
Reviewed the differences between partitioning and Z-Ordering as data layout optimization techniques in Databricks.

- Partitioning was identified as suitable for low-cardinality columns such as `Date` or `Country`.
- Partitioning creates sub-directories for each unique partition value, which can lead to a large number of small files if the partition column is not chosen carefully.

- Z-Ordering was reviewed as an optimization technique for high-cardinality columns such as `UserID`.
- Z-Ordering co-locates related data within the same set of files without creating additional directory levels.
- Observed that Z-Ordering is applied using the `OPTIMIZE` command and is not automatic; it must be executed explicitly on existing data.
- Noted that Z-Ordering is dynamic in nature, and adding too many columns to the Z-Order can reduce its effectiveness.
- Learned that Z-Ordering uses a Z-curve algorithm to organize data and improve data locality for query execution.

----

## Phase 3 — GenAI Concepts (Embeddings)

### 3.3. Vector Embeddings (Text to Numbers)
Reviewed the concept of vector embeddings and how textual data is represented as numerical vectors.

- Embeddings convert human-readable text into numerical vector representations.
- Semantic meaning is preserved within the vector space, allowing similar concepts to be closer together.
- Due to the high dimensionality of embedding vectors, direct distance measures can become less meaningful.
- Similarity between vectors is commonly computed using angular distance, calculated via cosine similarity.
- Cosine similarity values range from `-1` to `1`:
  - `1` indicates identical vectors.
  - `-1` indicates vectors pointing in opposite directions.
  - `0` indicates vectors are orthogonal (no similarity).

----

# ✔️ Day 3 Status: _CLEARED_
