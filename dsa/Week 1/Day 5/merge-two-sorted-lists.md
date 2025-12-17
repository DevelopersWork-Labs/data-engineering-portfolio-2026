# 21. Merge Two Sorted Lists - [leetcode](https://leetcode.com/problems/merge-two-sorted-lists/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *list = NULL, *curr, *temp;
        while (list1 && list2) {
            if (list1->val <= list2->val) {
                temp = list1;
                list1 = list1->next;
            } else {
                temp = list2;
                list2 = list2->next;
            }
            if (!list) {
                list = temp;
                curr = temp;
            } else {
                curr->next = temp;
                curr = curr->next;
            }
        }

        if (!list) {
            list = (list1 ? list1 : list2);
        } else {
            curr->next = (list1 ? list1 : list2);
        }

        return list;
    }
};
```
- **Time Complexity**: O(m+n)
- **Space Complexity**: O(1)
### 📝 Reviewer Notes

- **Iterative Approach**: The solution efficiently merges the two lists by comparing the head nodes and re-linking them, avoiding the stack overhead of recursion.
- **Pointer Management**: It uses a `curr` pointer to build the new list and a `temp` pointer to extract nodes from the input lists.
- **Edge Cases**: The code correctly handles cases where one list is empty or shorter than the other by appending the remainder of the non-empty list at the end.
- **Optimization Tip**: Using a dummy head node (`ListNode dummy(0); ListNode* curr = &dummy;`) would simplify the logic by eliminating the `if (!list)` conditional checks inside the loop.

