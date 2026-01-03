# 📚 104. Maximum Depth of Binary Tree - [leetcode](https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## 📖 Solution: C++
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
```
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$
### 📝 Reviewer Notes

- The recursive approach is concise and follows a post-order traversal pattern.
- **Time Complexity**: $O(n)$ because we visit each node exactly once.
- **Space Complexity**: $O(h)$, where $h$ is the height of the tree. In the worst case (a skewed tree), $h = n$, leading to $O(n)$ space on the call stack. In a balanced tree, it would be $O(\log n)$.
- An iterative solution using a queue (BFS) could also be used to find the depth level by level, which might be preferable if the tree is extremely deep to avoid stack overflow.
