# ✅ DSA Review — Day 10 (Binary Search Trees)

## 1. Validate Binary Search Tree (LeetCode #98)

### ✔️ Correctness
- Uses in-order traversal to verify the BST property.
- Correctly checks that the in-order traversal produces a strictly increasing sequence.
- Handles the empty tree case correctly.

### ✔️ Complexity
- Time Complexity: O(n), as each node is visited once.
- Space Complexity: O(n), due to storing all node values in a buffer.

### 🔍 Observations
- The solution is logically correct and easy to reason about.
- Space usage can be reduced by comparing the current node value with the previously visited value during traversal instead of storing all values.

### 💬 Interview Readiness
- Be prepared to explain why in-order traversal works for BST validation.
- Mention the alternative approach using min/max bounds for O(h) space.

### ✔️ Status
**PASS**

---

## 2. Kth Smallest Element in a BST (LeetCode #230)

### ✔️ Correctness
- Correctly leverages in-order traversal to retrieve elements in sorted order.
- Returns the k-th smallest element using 1-based indexing.

### ✔️ Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

### 🔍 Observations
- The traversal visits all nodes even if k is small.
- The approach is correct but does not take advantage of early stopping.

### 💬 Interview Readiness
- A more optimal approach tracks a counter during traversal and returns immediately once the k-th element is reached.
- Be ready to discuss how this reduces unnecessary traversal.

### ✔️ Status
**PASS (Correct, not optimized)**

---

## 3. Lowest Common Ancestor of a BST (LeetCode #235)

### ✔️ Correctness
- Correctly uses BST properties to identify the lowest common ancestor.
- Handles all cases: both nodes on the left, both on the right, or split across subtrees.

### ✔️ Complexity
- Time Complexity: O(h), where h is the height of the tree.
- Space Complexity:
  - Recursive version: O(h)
  - Iterative version: O(1)

### 🔍 Observations
- Both recursive and iterative implementations are correct.
- The iterative version avoids recursion overhead and is generally preferred.

### 💬 Interview Readiness
- Clearly explain the “split point” concept.
- Be prepared to justify iterative vs recursive trade-offs.

### ✔️ Status
**PASS**

---

# 📌 Overall Day 10 DSA Evaluation

| Problem | Evaluation |
|------|-----------|
| Validate Binary Search Tree | PASS |
| Kth Smallest Element in a BST | PASS (Not Optimized) |
| Lowest Common Ancestor of a BST | PASS |

### Final Verdict
**Day 10 DSA: CLEARED**

Core patterns demonstrated:
- In-order traversal of BSTs
- Leveraging BST ordering properties
- Recursive vs iterative traversal trade-offs
