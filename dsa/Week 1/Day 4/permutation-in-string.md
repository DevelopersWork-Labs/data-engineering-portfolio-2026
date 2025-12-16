# 📚 567. Permutation in String - [link](https://leetcode.com/problems/permutation-in-string/?envType=problem-list-v2&envId=vsm9u0sh&) 

## 📝 Problem Description

You are given two strings `s1` and `s2` of equal length. The task is to check if `s2` contains a permutation of `s1`.

## 📖 Solution: C++
```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size(), m = s2.size();
        if(n > m) return false;

        vector<int> freq(256, 0);
        for(char ch: s1){
            freq[ch]++;
        }

        int i = 0, j = 0;
        char ch;
        while(i < m && j < m){
            while(j < m){
                ch = s2[j++];
                freq[ch]--;
                if(freq[ch] < 0) break;
                if(j-i >= n && count(freq.begin(), freq.end(), 0) == 256)
                    return true;
            }
            while(i<j && freq[ch] < 0){
                freq[s2[i]]++;
                i++;
            }
            if(j-i >= n && count(freq.begin(), freq.end(), 0) == 256)
                return true;
        }

        return false;
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
### 📝 Reviewer Notes

- The solution uses a sliding window approach to find if `s2` contains a permutation of `s1`.
- The `while` loop iterates through the array, and the inner `while` loop extends the window by moving the right pointer `j` to the right until a 0 is encountered.
- The `result` variable is updated with the maximum length of the window found so far.
- The `while` loop then contracts the window by moving the left pointer `i` to the right until the number of flips is less than or equal to `k`.
- The `if` statement handles the case where the left pointer is equal to the right pointer and the current element is 0, and `k` is 0.
- The time complexity is O(n) as the `while` loop iterates through the array only once.
- The space complexity is O(1) as the solution only uses a few constant variables.
