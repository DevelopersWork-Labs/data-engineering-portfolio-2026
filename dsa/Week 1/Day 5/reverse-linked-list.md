# 206. Reverse Linked List - [leetcode](https://leetcode.com/problems/reverse-linked-list/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given the head of a singly linked list, reverse the list, and return the reversed list.

## 📖 Solution: C++
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *prev = NULL, *curr = head, *nxt;
        while(curr && curr->next){
            nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }
        if(curr)
            curr->next = prev;
        return curr;
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
### 📝 Reviewer Notes

- The iterative approach is optimal, providing $O(n)$ time and $O(1)$ space complexity.
- The logic correctly handles edge cases such as empty lists and single-node lists.
- **Refinement**: Using `while (curr)` instead of `while (curr && curr->next)` would simplify the implementation by handling the final node's pointer reversal inside the loop, eliminating the need for the post-loop conditional.

