# ✅ DSA Review — Day 5

## 1. Reverse Linked List (#206)

### ✔️ Correctness
- Implements an iterative pointer-reversal approach.
- Correctly reverses the list in a single pass.
- Handles edge cases such as empty lists and single-node lists.

### ✔️ Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

### 🔍 Observations
- The logic separates the final pointer reversal using a post-loop condition.
- This works correctly, but the loop can be simplified by iterating while `curr` is not null and handling all pointer updates inside the loop.

### 💬 Interview Readiness
- Be prepared to explain pointer manipulation (`prev`, `curr`, `next`) clearly.
- An alternative recursive solution can also be mentioned, though the iterative approach is preferred for O(1) space.

### ✔️ Status
**PASS**

---

## 2. Merge Two Sorted Lists (#21)

### ✔️ Correctness
- Correctly merges two sorted linked lists by re-linking existing nodes.
- Maintains sorted order throughout the merge process.
- Appends remaining nodes when one list is exhausted.

### ✔️ Complexity
- Time Complexity: O(m + n)
- Space Complexity: O(1)

### 🔍 Observations
- Uses explicit condition checks to initialize the result list.
- Logic is correct but slightly verbose due to repeated null checks.

### 💬 Interview Readiness
- Using a dummy head node would simplify pointer handling and reduce conditional branching.
- Be ready to explain why no new nodes are allocated and how in-place merging works.

### ✔️ Status
**PASS**

---

# 📌 Overall Day 5 DSA Evaluation

| Problem | Evaluation |
|------|-----------|
| Reverse Linked List | PASS |
| Merge Two Sorted Lists | PASS |

### Final Verdict
**Day 5 DSA: CLEARED**

Core patterns demonstrated:
- In-place linked list manipulation
- Iterative pointer traversal
- Merging sorted structures without extra space
