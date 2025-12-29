# ✅ DSA Review — Stack-Based Problems

## 1. Min Stack (#155)

### ✔️ Correctness
- Implements a dual-stack approach to support constant-time retrieval of the minimum element.
- Maintains a primary stack for values and an auxiliary stack to track minimums.
- Correctly updates the current minimum during push and pop operations.

### ✔️ Complexity
- Time Complexity: O(1) for all operations (`push`, `pop`, `top`, `getMin`)
- Space Complexity: O(n), due to the auxiliary stack storing minimum values.

### 🔍 Observations
- The `curr` variable caches the current minimum, avoiding repeated stack lookups.
- Dynamic allocation of stacks works correctly but could be simplified by using stack members directly instead of pointers.

### 💬 Interview Readiness
- Be ready to explain why an auxiliary stack is required.
- Mention that each element in the min-stack corresponds to the minimum at that depth of the main stack.

### ✔️ Status
**PASS**

---

## 2. Valid Parentheses (#20)

### Version 1: Stack + Explicit Matching

#### ✔️ Correctness
- Uses a stack to ensure proper ordering of opening and closing brackets.
- Correctly handles early termination when encountering invalid closures.

#### 🔍 Observations
- Uses `std::find` on a vector to identify opening brackets, which adds a small constant overhead.
- Explicit boolean matching logic is clear but verbose.

#### Status
**PASS**

---

### Version 2: Stack + Hash Map

#### ✔️ Correctness
- Uses an `unordered_map` to map closing brackets to their corresponding opening brackets.
- Simplifies matching logic and improves readability.

#### ✔️ Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

#### 💬 Interview Readiness
- The hash map approach is easier to extend and generally preferred in interviews.

#### ✔️ Status
**PASS (Preferred Implementation)**

---

## 3. Evaluate Reverse Polish Notation (#150)

### ✔️ Correctness
- Correctly evaluates arithmetic expressions written in Reverse Polish Notation.
- Uses a stack to store operands and applies operators as they are encountered.

### 🔍 Observations
- Pops operands before checking whether the token is an operator.
- The fallback logic correctly restores operands for numeric tokens, but the control flow is less intuitive than necessary.
- Operator detection relies on token length, which correctly handles multi-digit and negative numbers.

### ✔️ Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

### 💬 Interview Readiness
- A more conventional approach is to check if the token is an operator before popping operands.
- Be ready to explain operand order, especially for non-commutative operations like subtraction and division.

### ✔️ Status
**PASS (Correct, but can be simplified)**

---

# 📌 Overall DSA Evaluation

| Problem | Evaluation |
|------|-----------|
| Min Stack | PASS |
| Valid Parentheses | PASS |
| Evaluate RPN | PASS |

### Final Verdict
**DSA Problems: CLEARED**

Core patterns demonstrated:
- Stack-based state management
- Auxiliary data structures for constant-time queries
- Expression evaluation using LIFO semantics
