# 242. Valid Anagram - [link](https://leetcode.com/problems/valid-anagram/?envType=problem-list-v2&envId=vsm9u0sh&)

## Solution: C++
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(t.size() != s.size()) return false;
        
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        for(int i=0; i<s.size(); i++){
            if(s[i] != t[i]) return false;
        }
        return true;
    }
};
```
- **Time Complexity**: O(nlogn)
- **Space Complexity**: O(1)

## Solution: C++
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(t.size() != s.size()) return false;
        
        vector<int> ch_cnt(26, 0);
        for(char ch: s){
            ch_cnt[ch-'a']++;
        }
        for(char ch: t){
            ch_cnt[ch-'a']--;
        }
        
        for(int i=0; i<26; i++){
            if(ch_cnt[i] != 0) return false;
        }
        return true;
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
