# 155. Min Stack - [leetcode](https://leetcode.com/problems/min-stack/?envType=problem-list-v2&envId=vsm9u0sh&)

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