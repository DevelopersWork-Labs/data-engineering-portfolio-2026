## Phase 1.1 — DSA Progress

### 1. Contains Duplicate (#217)
Implemented two approaches:
- Hash-based lookup using an unordered_map for O(n) detection.
- Sorting-based comparison for O(n log n) with constant space.
Verified correctness and tested with multiple input patterns.

### 2. Valid Anagram (#242)
Solved using:
- Sorting both strings and comparing results.
- Character-frequency counting using a fixed 26-length array.
Validated logic by checking edge cases such as different lengths and repeated characters.

### 3. Group Anagrams (#49)
Implemented two grouping strategies:
- Sorted string as signature key.
- Character-frequency vector converted into a signature string.
Grouped strings by signatures using an unordered_map and verified grouped output manually.

## Phase 1.2 — Certification Progress

1. Learned about clustering and how liquid clustering works in databricks
2. Learned about data skew and how techniques like salting, liquid clustering will help minimize them
3. Different types of computes in databricks

Insights: In salting, we find one partition with big number of records and break it down. How you ask? We add a numeric value or a hash value to the partition key make it break down into multiple partitions.

## Phase 1.3 — System Design Progress

1. Row Oriented: Data is stored in rows, used in transactional system like OLTP
2. Column Oriented: Data is stored in columns, this will help in retriving data of same column faster. How you ask we only read underlying files that match the filter just by scanning the column header.
3. For OLAP (Analytics) we use columnar storage like parquet, delta etc., because we don't need entire row, we only need few columns.
