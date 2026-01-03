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

