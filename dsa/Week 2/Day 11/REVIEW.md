# ✅ DSA Review — Day 11 (Balanced Binary Trees)

## 1. Convert Sorted Array to Binary Search Tree (LeetCode #108)

### ✔️ Correctness
- Implements a recursive divide-and-conquer strategy.
- Correctly selects the middle element as the root to maintain height balance.
- Recursively constructs left and right subtrees from the remaining halves of the array.

### ✔️ Complexity
- Time Complexity: O(N), as each element is processed exactly once.
- Space Complexity: O(log N), assuming the recursion stack depth of a balanced tree.

### 🔍 Observations
- The midpoint is calculated using `(left + right) / 2`, which works for typical input sizes but could theoretically overflow in extreme cases.
- Conditional recursion (`left < mid`, `right > mid`) correctly prevents invalid subarray traversal.

### 💬 Interview Readiness
- Be prepared to explain why selecting the midpoint ensures height balance.
- Mention that this is essentially the same approach used when building balanced indices from sorted data.

### ✔️ Status
**PASS**

---

## 2. Balanced Binary Tree (LeetCode #110)

### ✔️ Correctness
- Uses a bottom-up DFS approach to compute subtree height and balance status simultaneously.
- Returns a `pair<bool, int>` where:
  - `bool` represents whether the subtree is balanced.
  - `int` represents the subtree height.
- Ensures the difference between left and right subtree heights does not exceed 1.

### ✔️ Complexity
- Time Complexity: O(N), since each node is visited exactly once.
- Space Complexity: O(H), where H is the tree height (recursion stack).

### 🔍 Observations
- The base case returns `{true, 1}` for `nullptr`, which shifts the height baseline but maintains correct relative comparisons.
- Combining height calculation and balance checking prevents repeated traversals.

### 💬 Interview Readiness
- Be ready to contrast this **bottom-up approach** with a **top-down approach** that recalculates heights and leads to O(N²).
- Clearly explain how returning both height and balance state enables a single traversal.

### ✔️ Status
**PASS**

---

# 📌 Overall Day 11 DSA Evaluation

| Problem | Evaluation |
|------|-----------|
| Convert Sorted Array to BST | PASS |
| Balanced Binary Tree | PASS |

### Final Verdict
**Day 11 DSA: CLEARED**

Core patterns demonstrated:
- Divide-and-conquer tree construction
- Bottom-up DFS for tree property validation
- Height-balanced tree reasoning