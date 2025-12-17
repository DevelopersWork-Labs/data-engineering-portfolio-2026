# 21. Merge Two Sorted Lists - [leetcode](https://leetcode.com/problems/merge-two-sorted-lists/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description
--

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
        while(list1 && list2){
            if(list1->val <= list2->val){
                temp = list1;
                list1 = list1->next;
            }
            else{
                temp = list2;
                list2 = list2->next;
            }
            if(!list){
                list = temp;
                curr = temp;
            } else {
                curr->next = temp;
                curr = curr->next;
            }
        }
        while(list1){
            if(!list){
                list = list1;
                curr = list1;
            } else {
                curr->next = list1;
                curr = curr->next;
            }
            list1 = list1->next;
        }
        while(list2){
            if(!list){
                list = list2;
                curr = list2;
            } else {
                curr->next = list2;
                curr = curr->next;
            }
            list2 = list2->next;
        }

        return list;
    }
};
```
- **Time Complexity**: O(m+n)
- **Space Complexity**: O(1)
### 📝 Reviewer Notes

--
