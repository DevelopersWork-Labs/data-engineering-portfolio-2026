# ✅ DSA Review — Day 4

## 1. Permutation in String (#567)

### ✔️ Correctness
- Uses a sliding window approach over `s2` while maintaining a frequency array derived from `s1`.
- Correctly handles the case where the length of `s1` exceeds `s2`.
- Expands the window by decrementing character frequencies and shrinks it when a frequency becomes negative.
- Ensures the window size is at least `n` (length of `s1`) before validating a permutation.

### 🔍 Observations
- The logic correctly enforces the window size constraint (`j - i >= n`) before checking for a valid permutation.
- The use of `count(freq.begin(), freq.end(), 0)` introduces a constant-factor scan of the frequency array.
- While the approach is correct, the repeated full scan makes the implementation more complex than necessary.

### 💬 Interview Readiness
- Be prepared to explain the sliding window invariant: the window represents a candidate permutation window of length `n`.
- A common alternative approach uses a `matched` counter instead of scanning the entire frequency array.

### ✔️ Complexity
- Time Complexity: O(n), with a constant overhead due to frequency array scans.
- Space Complexity: O(1).

### ✔️ Status
**PASS (Correct, but not optimal)**

---

## 2. Max Consecutive Ones III (#1004)

### ✔️ Correctness
- Correctly applies a sliding window technique with two pointers.
- Tracks the number of flipped zeros (`flp`) to ensure it does not exceed `k`.
- Updates the maximum window size whenever the window becomes invalid and is adjusted.

### 🔍 Observations
- The logic handles edge cases such as `k = 0` explicitly.
- The same behavior can be achieved with a simpler invariant (`flp <= k`) without special-case branching, but correctness is not affected.

### 💬 Interview Readiness
- Be ready to explain that the window always contains at most `k` zeros.
- Emphasize that both pointers move forward, guaranteeing linear time complexity.

### ✔️ Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

### ✔️ Status
**PASS**

---

# 📌 Overall Day 4 DSA Evaluation

| Problem | Evaluation |
|------|-----------|
| Permutation in String | PASS (Correct, not optimal) |
| Max Consecutive Ones III | PASS |

### Final Verdict
**Day 4 DSA: CLEARED**

Core patterns demonstrated:
- Sliding window with frequency balancing
- Window size and constraint management
- Two-pointer linear traversal
