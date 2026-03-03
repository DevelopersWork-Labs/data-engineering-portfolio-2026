# 📘 Week 2 — Day 10 Journal  

**Date:** 03/01/2026

----
## 🏗️ Phase 1: System Design (The "Spike" Scenario)

### 1. Backpressure
### 2. Batch Capping
### 3. Elasticity

----
## 🛠️ Phase 2: Project 2 — Streaming Ingestion

### 1. The Stream Source (Auto Loader)
### 2. Schema Evolution

----
## 📐 Phase 3: Algorithmic Engineering (DSA)

### 1. Validate Binary Search Tree (LeetCode #98)
Implemented a solution to validate whether a binary tree satisfies Binary Search Tree properties.

Performed an in-order traversal of the tree to collect node values.  
Verified that the traversal sequence is strictly increasing to confirm BST validity.  
Handled null nodes appropriately during traversal.
### 2. Lowest Common Ancestor of a BST (LeetCode #235)
Implemented an in-order traversal approach to find the k-th smallest element in a Binary Search Tree.

Traversed the tree in sorted order and stored node values in a list.  
Returned the element at the k-th position using 1-based indexing.
### 3. Kth Smallest Element in a BST (LeetCode #230)
Implemented logic to find the lowest common ancestor of two nodes in a Binary Search Tree.

Used BST ordering properties to traverse the tree:
- Moved left when both target nodes were smaller than the current node.
- Moved right when both target nodes were larger than the current node.
- Identified the current node as the lowest common ancestor when the targets diverged across subtrees.

Applied the approach until the ancestor node was found.

----
## Verification Question

**Question:**  
*If I delete the `checkpoint` directory of a running streaming job, what happens when I restart the job?*

**Answer:**  

----

# ✔️ Day 10 Status: _TO-DO_
