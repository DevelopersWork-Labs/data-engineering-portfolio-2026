# 📚 150. Evaluate Reverse Polish Notation - [leetcode](https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Return the value of the expression.

**Note** that:
- The valid operators are `+`, `-`, `*`, and `/`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

## 📖 Solution: C++
```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        int a,b;
        char sym;
        for(string &token: tokens){
            if(st.size() < 2){
                st.push(stoi(token));
                continue;
            }
            b = st.top();
            st.pop();
            a = st.top();
            st.pop();
            sym = (token.size() == 1) ? token[0] : '!';
            switch(sym){
                case '+':
                    st.push(a+b);
                    break;
                case '-':
                    st.push(a-b);
                    break;
                case '*':
                    st.push(a*b);
                    break;
                case '/':
                    st.push(a/b);
                    break;
                default:
                    st.push(a);
                    st.push(b);
                    st.push(stoi(token));
            }
        }
        return st.top();
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
### 📝 Reviewer Notes

- The solution correctly implements the stack-based evaluation of Reverse Polish Notation.
- **Logic**: The implementation uses an unconventional approach by popping two elements whenever the stack size is $\ge 2$ and then pushing them back in the `default` case if the token is a number. While functional, checking if the token is an operator *before* popping would be more efficient and readable.
- **Operator Handling**: The `sym` logic handles single-character operators. Note that negative numbers (e.g., `"-11"`) have a size $> 1$, so they correctly fall into the `default` case via the `!` placeholder.
- **Complexity**:
    - **Time Complexity**: $O(N)$, where $N$ is the number of tokens, as each token is processed once.
    - **Space Complexity**: $O(N)$ to store operands in the stack.

