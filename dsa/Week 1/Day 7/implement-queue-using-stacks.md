# 📚 232. Implement Queue using Stacks - [leetcode](https://leetcode.com/problems/implement-queue-using-stacks/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Notes**:
- You must use only standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

## 📖 Solution: C++
```cpp
class MyQueue {
    stack<int> *st1, *st2;
public:
    MyQueue() {
        st1 = new stack<int>();
        st2 = new stack<int>();
    }
    
    void push(int x) {
        while(!st1->empty()){
            st2->push(st1->top());
            st1->pop();
        }
        st1->push(x);
        while(!st2->empty()){
            st1->push(st2->top());
            st2->pop();
        }
    }
    
    int pop() {
        int value = st1->top();
        st1->pop();
        return value;
    }
    
    int peek() {
        return st1->top();
    }
    
    bool empty() {
        return st1->empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
### 📝 Reviewer Notes

- The implementation uses a two-stack approach where the `push` operation is $O(N)$ to ensure that the elements are stored in the correct queue order (FIFO) within `st1`.
- By reversing the elements into `st2` and back during every `push`, the `pop` and `peek` operations are optimized to $O(1)$.
- **Alternative Optimization**: An amortized $O(1)$ approach for all operations can be achieved by only transferring elements from an "input" stack to an "output" stack when the "output" stack is empty during a `pop` or `peek` call.
- Ensure that the constructor initializes the stack pointers and the destructor handles memory deallocation to prevent leaks.

## 📖 Solution: C++
```cpp
class MyQueue {
    stack<int> *in, *out;
    void shuffle(){
        while(!in->empty()){
            out->push(in->top());
            in->pop();
        }
    }
public:
    MyQueue() {
        in = new stack<int>();
        out = new stack<int>();
    }
    
    void push(int x) {
        in->push(x);
    }
    
    int pop() {
        if(out->empty())
            shuffle();
        int value = out->top();
        out->pop();
        return value;
    }
    
    int peek() {
        if(out->empty())
            shuffle();
        return out->top();
    }
    
    bool empty() {
        return in->empty() && out->empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```
- **Time Complexity**: Amortized $O(1)$
- **Space Complexity**: $O(N)$
### 📝 Reviewer Notes

- This implementation follows the amortized $O(1)$ approach, where `push` is always $O(1)$ and `pop`/`peek` are $O(1)$ on average.
- Elements are lazily transferred from the `in` stack to the `out` stack only when the `out` stack is empty, reducing unnecessary operations compared to the first solution.
- The `shuffle` helper function encapsulates the transfer logic, ensuring that the FIFO order is maintained efficiently.
- As with the previous solution, ensure a destructor is implemented to free the memory allocated for the `in` and `out` stack pointers.
