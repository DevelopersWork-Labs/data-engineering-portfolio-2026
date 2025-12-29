# 📚 20. Valid Parentheses - [leetcode](https://leetcode.com/problems/valid-parentheses/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

## 📖 Solution: C++
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
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
### 📝 Reviewer Notes

- The solution uses a standard stack-based approach to ensure that the most recently opened bracket is the first one to be closed.
- Using `std::find` on a vector to identify opening brackets works well for a small number of character types but adds a constant factor to the time complexity.
- The explicit boolean logic for matching pairs is clear but could be more concisely handled with a hash map to map closing brackets to their corresponding opening counterparts.

## 📖 Solution: C++
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
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
### 📝 Reviewer Notes

- Utilizing an `unordered_map` improves readability and provides $O(1)$ average time complexity for lookups.
- The use of `static` for the hash map is a performance optimization that ensures the map is initialized only once across multiple function calls.
- This approach is more scalable and easier to maintain if additional types of brackets need to be supported in the future.

