## Phase 1.1 — DSA Progress

### 1. Contains Duplicate (#217)
Implemented two approaches:
- Hash-based lookup using an unordered_map to detect duplicates in O(n) time.
- Sorting-based comparison to identify adjacent duplicates in O(n log n) time with constant extra space.
Verified correctness using different input patterns.

### 2. Valid Anagram (#242)
Solved using:
- Sorting both input strings and comparing the results.
- Character-frequency counting using a fixed-size (26) integer array.
Validated logic with edge cases such as unequal lengths and repeated characters.

### 3. Group Anagrams (#49)
Implemented two grouping strategies:
- Using sorted strings as signature keys.
- Using character-frequency vectors converted into signature strings.
Grouped strings by signatures using an unordered_map and manually verified grouped outputs.

---

## Phase 1.2 — Certification Progress

- Learned about clustering concepts in Databricks and how liquid clustering works.
- Studied data skew and how techniques like salting and liquid clustering help reduce skew.
- Reviewed different types of compute options available in Databricks.

**Insights:**  
In salting, a skewed partition with a large number of records is broken down by adding a numeric or hash-based value to the partition key, causing the data to be distributed across multiple partitions.

---

## Phase 1.3 — System Design Progress

- **Row-Oriented Storage:** Data is stored row by row and is commonly used in transactional systems (OLTP).
- **Column-Oriented Storage:** Data is stored column-wise, enabling faster access when querying specific columns by scanning column metadata.
- Columnar formats such as Parquet and Delta are used for OLAP (analytics) workloads because queries typically require only a subset of columns rather than entire rows.
