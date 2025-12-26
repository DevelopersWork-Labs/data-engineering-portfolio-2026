# 20. Valid Parentheses - [leetcode](https://leetcode.com/problems/valid-parentheses/?envType=problem-list-v2&envId=vsm9u0sh&)

```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        vector<char> open{'(', '{', '['};
        for(char c: s){
            if(find(open.begin(), open.end(), c) != open.end()){
                st.push(c);
                continue;
            }
            if(st.size() < 1) return false;
            bool expr = (
                (st.top() == '(' && c == ')')
                || (st.top() == '{' && c == '}')
                || (st.top() == '[' && c == ']')
            );
            if(!expr) return false;
            st.pop();
        }

        return st.size() == 0;
    }
};
```

```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        static unordered_map<char, char> hash{{')','('}, {'}','{'}, {']','['}};
        for(char c: s){
            if(hash.find(c) == hash.end()){
                st.push(c);
                continue;
            }
            if(st.empty()) return false;
            if(hash[c] != st.top()) return false;
            st.pop();
        }

        return st.empty();
    }
};
```

