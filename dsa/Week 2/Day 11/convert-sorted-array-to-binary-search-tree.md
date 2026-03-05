# 📚 108. Convert Sorted Array to Binary Search Tree - [leetcode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree (BST).

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
    TreeNode* balancedBinaryTree(vector<int>& nums, int left, int right){
        int mid = (left+right)/2;
        TreeNode* root = new TreeNode(nums[mid]);
        if(left < mid)
            root->left = balancedBinaryTree(nums, left, mid-1);
        if(right > mid)
            root->right = balancedBinaryTree(nums, mid+1, right);
        return root;
    }
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return balancedBinaryTree(nums, 0, nums.size()-1);
    }
};
```
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(logN)$
### 📝 Reviewer Notes

- **Approach**: The solution uses a recursive divide-and-conquer strategy. By consistently picking the middle element of the current subarray as the root, we ensure that the number of nodes in the left and right subtrees differs by at most one, maintaining a height-balanced BST.
- **Base Cases**: The implementation uses conditional checks (`left < mid` and `right > mid`) to prevent out-of-bounds recursion, effectively handling the leaf nodes.
- **Efficiency**: 
    - **Time**: Each element in the array is processed exactly once to create a node, resulting in $O(N)$ time.
    - **Space**: Since the tree is guaranteed to be balanced, the recursion stack depth is $O(\log N)$.

