# ✅ DSA Review — Day 3

## 1. Longest Substring Without Repeating Characters (#3)

### ✔️ Correctness
- Correctly implements the sliding window technique.
- Uses two pointers (`i`, `j`) to maintain a window of unique characters.
- A fixed-size frequency array (size 256) tracks character occurrences.
- Ensures each character is added and removed from the window at most once.

### ✔️ Complexity
- Time Complexity: O(n), as both pointers traverse the string linearly.
- Space Complexity: O(1), due to the constant-sized frequency array.

### 🔍 Observations
- The variable `ch` captures the character that caused a repetition and is used to control window shrinkage.
- The logic is sound, though slightly non-standard compared to the typical “last seen index” approach.
- Readability could be improved, but correctness is not impacted.

### 💬 Interview Readiness
- Be prepared to explain the sliding window invariant: the window always contains unique characters.
- You may also mention an alternative approach using a hash map of last-seen indices.

### ✔️ Status
**PASS**

---

## 2. Best Time to Buy and Sell Stock (#121)

### Version 1: Nested Loop Attempt

#### ⚠️ Correctness Issues
- The logic prematurely breaks when a negative profit is encountered.
- Updating `i = j` skips valid buying opportunities.
- Does not correctly model the “buy once, sell later” constraint.

#### ⚠️ Complexity
- Time Complexity degrades to O(n²) in the worst case.
- Inefficient for large input sizes.

#### Status
**INCORRECT / NOT ACCEPTABLE**

---

### Version 2: Optimized Single-Pass Solution

#### ✔️ Correctness
- Correctly tracks the minimum price encountered so far.
- Updates maximum profit using the current price minus the minimum price.
- Ensures buy happens before sell.

#### ✔️ Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

#### 💬 Interview Readiness
- This solution aligns with standard interview expectations.
- Clearly demonstrates greedy reasoning and single-pass optimization.

#### ✔️ Status
**PASS (Primary Solution)**

---

# 📌 Overall Day 3 DSA Evaluation

| Problem | Evaluation |
|------|-----------|
| Longest Substring Without Repeating Characters | PASS |
| Best Time to Buy and Sell Stock | PASS (Optimized Version) |

### Final Verdict
**Day 3 DSA: CLEARED**

Core patterns covered:
- Sliding window with two pointers
- Frequency-based window maintenance
- Greedy single-pass optimization
