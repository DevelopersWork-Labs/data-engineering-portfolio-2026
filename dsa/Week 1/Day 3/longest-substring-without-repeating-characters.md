# 📚 3. Longest Substring Without Repeating Characters - [link](https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given a string `s`, find the length of the longest substring without repeating characters.

## 📖 Solution: C++
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> freq(256, 0);
        int result = 0, n = s.size();

        int i=0, j=0, ch;
        while(i < n && j < n){
            while(j < n){
                ch = s[j];
                freq[ch]++;
                if(freq[ch] > 1) break;
                j++;
            }
            result = max(result, j - i);
            while(i < j && freq[ch] > 1){
                freq[s[i]]--;
                i++;
            }
            j++;
        }

        return result;
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
### 📝 Reviewer Notes

This solution correctly implements the sliding window technique. It uses a frequency array to keep track of character occurrences within the current window `[i, j)`. The window expands by incrementing `j` and shrinks by incrementing `i` when a duplicate character is encountered. The time complexity is O(n) because both `i` and `j` pointers traverse the string at most once. Space complexity is O(1) as the `freq` array size is fixed (256 for ASCII characters).

A minor point for clarity: the variable `ch` is updated inside the first `while` loop with `s[j]`, and then used in the subsequent `while` loop that shrinks the window. This works, but it specifically targets the character that *just caused* the repetition. The logic correctly handles shrinking the window until that specific character's count is back to 1.
