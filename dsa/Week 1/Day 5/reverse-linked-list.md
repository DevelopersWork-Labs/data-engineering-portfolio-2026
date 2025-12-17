# 206. Reverse Linked List - [leetcode](https://leetcode.com/problems/reverse-linked-list/?envType=problem-list-v2&envId=vsm9u0sh&)

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