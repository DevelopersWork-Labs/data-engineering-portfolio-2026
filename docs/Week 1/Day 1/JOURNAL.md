## Phase 1 — DSA Progress

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
