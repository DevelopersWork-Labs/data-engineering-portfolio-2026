# 📚 110. Balanced Binary Tree - [leetcode](https://leetcode.com/problems/balanced-binary-tree/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given a binary tree, determine if it is height-balanced.

A **height-balanced binary tree** is defined as a binary tree in which the depth of the two subtrees of **every** node never differs by more than 1.

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
    pair<bool, int> dfs(TreeNode* root){
        if(!root) return {true, 1};
        
        pair<bool, int> 
            left = dfs(root->left),
            right = dfs(root->right);
        
        return {
            left.first && right.first && (abs(left.second-right.second) <= 1), 
            1+max(left.second, right.second)
        };
    }
public:
    bool isBalanced(TreeNode* root) {
        return dfs(root).first;
    }
};
```
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(logN)$
### 📝 Reviewer Notes

- The solution uses a **bottom-up DFS** approach, which is more efficient than a top-down approach because it calculates the height and balance status in a single pass ($O(N)$).
- By returning a `pair<bool, int>`, we avoid redundant calls to a separate `height` function, preventing the complexity from degrading to $O(N^2)$.
- The base case returns a height of `1` for `nullptr`, meaning a leaf node will have a height of `2`. While unconventional (usually `0`), the relative difference logic remains correct.
- **Space Complexity**: The $O(\log N)$ space complexity assumes a balanced tree for the recursion stack; in the worst case (a skewed tree), it would be $O(N)$.


