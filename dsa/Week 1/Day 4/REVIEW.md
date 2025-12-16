# ✅ DSA Review — Day 4

## 1. Permutation in String (#567)

### ✔️ Correctness
- Uses a sliding window approach over `s2` while tracking character frequencies from `s1`.
- Correctly handles the case where `s1` is longer than `s2`.
- Adjusts the window when character counts fall below zero, indicating an invalid permutation window.

### ⚠️ Observations
- The use of `count(freq.begin(), freq.end(), 0)` inside the sliding window introduces an extra O(256) scan on each iteration.
- While 256 is constant, this approach is inefficient and obscures the core sliding window invariant.
- The logic is correct but more complex than necessary.

### 💬 Interview Readiness
- Be prepared to explain the window invariant and how frequency balancing determines a valid permutation.
- A more common approach is to track a `matched` counter instead of scanning the full frequency array.

### ✔️ Complexity
- Time Complexity: O(n) (with a constant-factor overhead due to repeated scans).
- Space Complexity: O(1).

### ✔️ Status
**PASS (Correct but not optimal)**

---

## 2. Max Consecutive Ones III (#1004)

### ✔️ Correctness
- Correctly applies the sliding window technique with two pointers.
- Tracks the number of flipped zeros (`flp`) to ensure it does not exceed `k`.
- Expands and contracts the window to maintain validity and track the maximum window size.

### 🔍 Observations
- The special-case handling when `i == j` and `k == 0` works correctly but adds extra branching.
- The same logic can be simplified by allowing the window to expand fully and shrinking only when `flp > k`.

### 💬 Interview Readiness
- Be ready to explain the sliding window invariant: the window contains at most `k` zeros.
- A simpler version of this logic is often preferred in interviews for clarity.

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

Core patterns covered:
- Sliding window with frequency balancing
- Two-pointer window expansion and contraction
- Constraint-based window maintenance
