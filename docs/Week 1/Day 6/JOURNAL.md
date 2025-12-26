# 📘 Week 1 — Day 6 Journal  

**Date:** 27/12/2025

----
## 🏗️ Phase 1: Project 1 Implementation (Bronze Layer)

**PLACEHOLDER**

----
## 🛠️ Phase 2: DSA Workshop (Stacks)

### 2.3. Valid Parentheses (LeetCode #20)
Implemented a stack-based solution to validate balanced parentheses in a string.

Traversed the input string character by character.  
Pushed opening brackets onto a stack and matched closing brackets against the top of the stack.  
Popped elements from the stack when a valid matching pair was found.  
Verified validity by ensuring the stack was empty after processing the entire string.

### 2.4. Min Stack (LeetCode #155)
Implemented a stack data structure supporting constant-time retrieval of the minimum element.

Used two stacks:
- One stack to store the actual values.
- A secondary stack to track the minimum value at each level.

Updated the minimum-tracking stack during push and pop operations to keep the current minimum in sync with the main stack.

### 2.5. Evaluate Reverse Polish Notation (LeetCode #150)
Implemented a stack-based evaluator for arithmetic expressions in Reverse Polish Notation.

Iterated through the list of tokens:
- Pushed numeric operands onto the stack.
- Applied arithmetic operations by popping operands from the stack when an operator was encountered.
- Pushed the computed result back onto the stack.

Returned the final value remaining on the stack after processing all tokens.

---
## 🤖 Phase 3: GenAI Infrastructure Prep

**PLACEHOLDER**

----
## Verification Question

**Question:**  
*If I process a CSV file today with 5 columns, and tomorrow I receive a CSV with 6 columns, what happens to my Bronze Delta Table if `mergeSchema` is set to `false`?*

**Answer:**  
- ...

----

# ✔️ Day 6 Status: _IN-PROGRESS_