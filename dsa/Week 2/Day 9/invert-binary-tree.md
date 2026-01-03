# 📚 226. Invert Binary Tree - [leetcode](https://leetcode.com/problems/invert-binary-tree/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given the root of a binary tree, invert the tree, and return its root.

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
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return root;
        TreeNode* temp = invertTree(root->left);
        root->left = invertTree(root->right);
        root->right = temp;
        return root;
    }
};
```
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$
### 📝 Reviewer Notes

- The solution uses a recursive Depth-First Search (DFS) approach to traverse the tree and swap the left and right children of every node.
- **Base Case**: If the current node is `nullptr`, the recursion stops and returns `nullptr`.
- **Recursive Step**: The function recursively calls itself on the left and right children. The returned inverted subtrees are then swapped and assigned to the current node's `right` and `left` pointers respectively.
- **Efficiency**:
    - **Time Complexity**: $O(n)$, where $n$ is the number of nodes in the tree, as each node is visited exactly once.
    - **Space Complexity**: $O(h)$, where $h$ is the height of the tree, representing the maximum depth of the recursion stack. In the worst case (a skewed tree), this is $O(n)$.
- **Alternative**: An iterative approach using a `std::queue` (BFS) or `std::stack` (DFS) could be implemented to avoid potential stack overflow for extremely deep trees.
