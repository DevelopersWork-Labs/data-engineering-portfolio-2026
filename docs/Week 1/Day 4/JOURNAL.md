# 📘 Week 1 — Day 4 Journal  

**Date:** 17/12/2025

----

## Phase 1 — Algorithmic Engineering (DSA)

### 1.1. Permutation in String (#567)
Implemented a sliding window approach to check whether a permutation of one string exists within another string.

Initialized a frequency array based on characters in the first string.  
Traversed the second string using two pointers, decrementing character frequencies as the window expanded.  
When a character frequency became invalid, adjusted the window by moving the left pointer and restoring frequencies.  
Validated permutation existence by ensuring the window size matched the length of the first string.

### 1.2. Max Consecutive Ones III (#1004)
Solved using a sliding window technique with two pointers.

Expanded the window while tracking the number of flipped zeros allowed by the constraint.  
When the number of flipped zeros exceeded the limit, contracted the window from the left until the constraint was satisfied.  
Tracked and updated the maximum window size representing the longest sequence of ones after allowed flips.

----

## Phase 2 — Platform Architecture (Skew Handling & Optimization)

### 2.3.1. Join Skew Simulation and Salted Join

Prepared two datasets to simulate join skew:
- A small lookup dataset (`df_small`) generated using a fixed range and grouped identifiers.
- A large fact dataset (`df_large`) created by combining two datasets with an intentionally skewed `user_id` distribution.

Analyzed the distribution of `user_id` values in the large dataset to observe skew, where certain keys appeared significantly more frequently than others.

### 2.3.2 Baseline Join Observation
Performed a standard inner join between the small and large datasets on `user_id`.

Observed that highly frequent `user_id` values dominated the join output, resulting in uneven grouping counts and indicating skewed join behavior.

### 2.3.3 Salted Join Implementation
Applied a salting technique to mitigate join skew.

- Introduced a `salt` column with a fixed range of values.
- Expanded the small dataset by duplicating each row across all possible salt values.
- Added a randomly generated salt value to each row in the large dataset.

Performed a join using a composite key (`user_id`, `salt`) between the salted datasets.

### 2.3.4 Post-Salting Observation
Grouped the joined output by `user_id` and `salt` and analyzed record counts.

Observed that previously skewed `user_id` values were distributed across multiple salt values, resulting in a more balanced distribution of join records.

----

## GenAI Architecture (Vector Stores)

### 3.4. The Vector Database & HNSW
Reviewed how vector databases are used to perform similarity search on embedding vectors.

- Embeddings convert text into numerical vectors, after which efficient search becomes the primary challenge.
- A brute-force similarity search compares the query vector against all stored vectors, resulting in O(n) time complexity.
- To reduce query latency, vector databases use Approximate Nearest Neighbor (ANN) techniques that trade exact accuracy for speed.
- ANN search returns results that are close enough to the true nearest neighbors, prioritizing low latency.
- One commonly used ANN algorithm is HNSW (Hierarchical Navigable Small World).
- HNSW organizes vectors into multiple layers, where upper layers enable fast coarse-grained navigation and lower layers refine the search.
- This hierarchical structure is similar to navigating a city using highways and flyovers first, then local roads for precise routing.
- Using HNSW reduces the average search complexity to approximately O(log n).

----

# ✔️ Day 4 Status: _CLEARED_
