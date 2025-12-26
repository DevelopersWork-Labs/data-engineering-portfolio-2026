# 155. Min Stack - [leetcode](https://leetcode.com/problems/min-stack/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

## 📖 Solution: C++
```cpp
class MinStack {
    stack<int> *st, *mst;
    int curr;
public:
    MinStack() {
        st = new stack<int>();
        mst = new stack<int>();
        curr = INT_MAX;
    }
    
    void push(int val) {
        st->push(val);
        curr = min(curr, val);
        mst->push(curr);
    }
    
    void pop() {
        st->pop();
        mst->pop();
        if(mst->empty())
            curr = INT_MAX;
        else
            curr = mst->top();
    }
    
    int top() {
        return st->top();
    }
    
    int getMin() {
        return curr;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
### 📝 Reviewer Notes

- The implementation utilizes a dual-stack approach to maintain the minimum element in constant time.
- `st` stores the actual values, while `mst` (min-stack) tracks the minimum value encountered up to that point in the stack.
- All operations—`push`, `pop`, `top`, and `getMin`—achieve $O(1)$ time complexity.
- The `curr` member variable is used to cache the current minimum, ensuring that `getMin()` is efficient, while being properly updated from the auxiliary stack during `pop` operations.
- The space complexity is $O(n)$ because the auxiliary stack grows proportionally with the number of elements pushed.
