# 📚 100. Same Tree - [leetcode](https://leetcode.com/problems/same-tree/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<TreeNode*> a1 = {p}, a2 = {q};
        int n;

        while(!a1.empty() && !a2.empty()){
            vector<TreeNode*> b1, b2;
            n = a1.size();
            for(int i=0; i<n; i++){
                if(a1[i] == a2[i]) continue;
                if(!a1[i] || !a2[i]) return false;
                if(a1[i]->val != a2[i]->val) return false;
                b1.push_back(a1[i]->left);
                b1.push_back(a1[i]->right);
                b2.push_back(a2[i]->left);
                b2.push_back(a2[i]->right);
            }
            a1 = b1;
            a2 = b2;
        }

        return a1.empty() && a2.empty();
    }
};
```
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$
### 📝 Reviewer Notes

- The solution correctly implements an iterative BFS (level-order traversal) to compare both trees simultaneously.
- It efficiently handles structural differences and value mismatches by comparing nodes at each level.
- While the iterative approach is robust, a recursive DFS solution would provide a more concise and idiomatic implementation for this problem.
