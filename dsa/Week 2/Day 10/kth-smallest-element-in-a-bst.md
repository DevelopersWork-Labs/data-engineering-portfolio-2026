# 📚 230. Kth Smallest Element in a BST - [leetcode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given the `root` of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

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
    vector<int> buffer;
    void inordertraversal(TreeNode* root){
        if(!root) return;
        if(root->left)
            inordertraversal(root->left);
        buffer.push_back(root->val);
        if(root->right)
            inordertraversal(root->right);
    }
public:
    int kthSmallest(TreeNode* root, int k) {
        inordertraversal(root);
        return buffer[k-1];
    }
};
```
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$
### 📝 Reviewer Notes

- The solution correctly leverages the property that an in-order traversal of a Binary Search Tree (BST) visits nodes in ascending order.
- **Space Optimization**: Currently, the solution uses $O(n)$ space to store all node values in a vector. This can be optimized to $O(h)$ (where $h$ is the height of the tree) by using a counter to track the number of nodes visited and returning the value immediately upon reaching the $k$-th element.
- **Early Exit**: The current `inordertraversal` visits every node in the tree regardless of the value of $k$. Implementing an early exit once the $k$-th smallest element is found would improve performance, especially for small values of $k$ in large trees.
