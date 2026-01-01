# ✅ DSA Review — Day 7

## 1. Number of Islands (#200)

### ✔️ Correctness
- Implements a Depth First Search (DFS) approach to identify and count connected components in a 2D grid.
- Correctly treats horizontal and vertical adjacency as part of the same island.
- Modifies the input grid in-place to mark visited land cells, preventing reprocessing.

### ✔️ Complexity
- Time Complexity: O(M × N), where M and N are the grid dimensions.
- Space Complexity: O(1) auxiliary space, excluding recursion stack usage.

### 🔍 Observations
- In-place marking avoids the need for an additional `visited` matrix.
- Recursion depth may grow to O(M × N) in the worst case (entire grid filled with land).

### 💬 Interview Readiness
- Be prepared to explain DFS vs BFS trade-offs.
- Mention stack overflow risks for large grids and the iterative BFS alternative.

### ✔️ Status
**PASS**

---

## 2. Implement Queue using Stacks (#232)

### Version 1: Push-Heavy Two-Stack Approach

#### ✔️ Correctness
- Correctly maintains FIFO order using two stacks.
- Reorders elements during each `push` operation to keep the front element accessible.

#### ✔️ Complexity
- Push: O(N)
- Pop / Peek: O(1)
- Space Complexity: O(N)

#### 🔍 Observations
- Guarantees constant-time dequeue operations at the cost of expensive enqueue operations.
- Uses eager reordering, which leads to unnecessary data movement.

#### Status
**PASS (Correct but not optimal)**

---

### Version 2: Amortized Two-Stack Approach

#### ✔️ Correctness
- Uses separate `in` and `out` stacks to preserve FIFO order.
- Transfers elements only when required during `pop` or `peek`.

#### ✔️ Complexity
- Push: O(1)
- Pop / Peek: Amortized O(1)
- Space Complexity: O(N)

#### 💬 Interview Readiness
- This is the preferred and expected solution in interviews.
- Clearly demonstrates amortized analysis and lazy evaluation.

#### ✔️ Status
**PASS (Primary Solution)**

---

# 📌 Overall Day 7 DSA Evaluation

| Problem | Evaluation |
|------|-----------|
| Number of Islands | PASS |
| Implement Queue using Stacks | PASS (Amortized Solution) |

### Final Verdict
**Day 7 DSA: CLEARED**

Core patterns demonstrated:
- Graph traversal using DFS
- Connected component identification
- Stack-based simulation of queue behavior
- Amortized complexity analysis
