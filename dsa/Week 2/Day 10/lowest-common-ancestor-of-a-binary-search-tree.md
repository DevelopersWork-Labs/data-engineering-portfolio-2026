# 📚 235. Lowest Common Ancestor of a Binary Search Tree - [leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

## 📖 Solution: C++
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root) return root;
        if(p->val < root->val && q->val < root->val) return lowestCommonAncestor(root->left, p, q);
        if(p->val > root->val && q->val > root->val) return lowestCommonAncestor(root->right, p, q);
        return root;
    }
};
```
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$
### 📝 Reviewer Notes

- The solution leverages the fundamental property of a **Binary Search Tree (BST)**: for any given node, all nodes in the left subtree have smaller values, and all nodes in the right subtree have larger values.
- **Logic**: 
    - If both `p` and `q` are smaller than the current `root`, the LCA must be in the left subtree.
    - If both are larger, the LCA must be in the right subtree.
    - If one is smaller and the other is larger (or one is equal to the root), the current `root` is the "split point" and thus the Lowest Common Ancestor.
- **Complexity**:
    - **Time**: $O(h)$, where $h$ is the height of the tree. In the worst case (a skewed tree), this is $O(n)$.
    - **Space**: $O(h)$ due to the recursive call stack.
- **Optimization**: This can be implemented **iteratively** to achieve $O(1)$ auxiliary space complexity, as we only need to traverse down a single path without needing to backtrack.

## 📖 Solution: C++
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root) return root;

        while(root){
            if(p->val < root->val && q->val < root->val) 
                root = root->left;
            else if(p->val > root->val && q->val > root->val) 
                root = root->right;
            else break;
        }
        return root;
    }
};
```
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$
### 📝 Reviewer Notes

- This version implements the **iterative approach**, which is generally preferred for this problem to avoid potential stack overflow on very deep or skewed trees.
- **Logic**:
    - We traverse the tree starting from the root using a `while` loop.
    - If both `p` and `q` values are smaller than the current node's value, we move to the `left` child.
    - If both are larger, we move to the `right` child.
    - The loop terminates as soon as we find a "split" (one value is smaller and the other is larger) or we encounter one of the target nodes themselves.
- **Complexity**:
    - **Time**: $O(h)$, where $h$ is the height of the tree.
    - **Space**: $O(1)$, as it only uses a constant amount of extra space for the traversal pointer.
