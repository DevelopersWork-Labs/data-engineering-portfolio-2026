# 📚 98. Validate Binary Search Tree - [leetcode](https://leetcode.com/problems/validate-binary-search-tree/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:

The left subtree of a node contains only nodes with keys **strictly less than** the node's key.
The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
Both the left and right subtrees must also be valid BSTs.

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
    void inOrderTraversal(TreeNode* root){
        if(root->left)
            inOrderTraversal(root->left);
        buffer.push_back(root->val);
        if(root->right)
            inOrderTraversal(root->right);
    }
public:
    bool isValidBST(TreeNode* root) {
        if(!root) return true;
        inOrderTraversal(root);
        for(int i=1; i<buffer.size(); i++)
            if(buffer[i-1] >= buffer[i]) return false;
        return true;
    }
};
```
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$
### 📝 Reviewer Notes

- **Logic**: The solution leverages the property that an in-order traversal of a valid Binary Search Tree (BST) must result in a strictly increasing sequence of values.
- **Efficiency**: 
    - **Time**: $O(n)$ since every node is visited exactly once.
    - **Space**: $O(n)$ because all node values are stored in a vector.
- **Optimization**: To improve space complexity to $O(h)$ (where $h$ is the height of the tree), one could perform the in-order traversal and compare each node's value with the previously visited node's value directly, instead of using an intermediate buffer.
- **Edge Cases**: Correctly handles the empty tree case and ensures strict inequality (no duplicate values allowed in a standard BST).

