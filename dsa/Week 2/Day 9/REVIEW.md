# ✅ DSA Review — Day 9 (Binary Trees)

## 1. Same Tree (LeetCode #100)

### ✔️ Correctness
- Correctly compares two binary trees for both structural and value equality.
- Uses an iterative BFS-style traversal to process both trees level by level.
- Handles null-node cases and value mismatches appropriately.

### ✔️ Complexity
- Time Complexity: O(n), where n is the number of nodes.
- Space Complexity: O(n), due to storing nodes at each level.

### 🔍 Observations
- The iterative approach is robust and avoids recursion depth issues.
- The implementation uses temporary vectors for each level, which is correct but slightly verbose.
- A recursive DFS solution could provide a more concise alternative.

### 💬 Interview Readiness
- Be prepared to explain both BFS and DFS approaches.
- Clearly articulate how structural equality is enforced alongside value checks.

### ✔️ Status
**PASS**

---

## 2. Invert Binary Tree (LeetCode #226)

### ✔️ Correctness
- Correctly inverts the binary tree by swapping left and right subtrees at each node.
- Uses a recursive DFS approach with a clear base case.

### ✔️ Complexity
- Time Complexity: O(n), as each node is visited once.
- Space Complexity: O(h), where h is the height of the tree due to recursion stack usage.

### 🔍 Observations
- The recursion is clean and idiomatic for this problem.
- For very deep or skewed trees, recursion depth could become an issue.

### 💬 Interview Readiness
- Mention iterative BFS or DFS alternatives if stack overflow concerns arise.
- Be clear about how recursion propagates inverted subtrees upward.

### ✔️ Status
**PASS**

---

## 3. Maximum Depth of Binary Tree (LeetCode #104)

### ✔️ Correctness
- Correctly computes the maximum depth using a recursive post-order traversal.
- Returns `0` for a null tree and increments depth appropriately for each level.

### ✔️ Complexity
- Time Complexity: O(n)
- Space Complexity: O(h), where h is the height of the tree.

### 🔍 Observations
- The solution is concise and easy to reason about.
- Works efficiently for both balanced and unbalanced trees.

### 💬 Interview Readiness
- Be ready to contrast DFS (recursive) and BFS (level-order) approaches.
- Highlight differences in space usage for balanced vs skewed trees.

### ✔️ Status
**PASS**

---

# 📌 Overall Day 9 DSA Evaluation

| Problem | Evaluation |
|------|-----------|
| Same Tree | PASS |
| Invert Binary Tree | PASS |
| Maximum Depth of Binary Tree | PASS |

### Final Verdict
**Day 9 DSA: CLEARED**

Core patterns demonstrated:
- Tree traversal using DFS and BFS
- Recursive problem decomposition
- Structural and value-based tree comparisons
