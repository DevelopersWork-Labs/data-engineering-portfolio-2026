# 49. Group Anagrams - [link](https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=vsm9u0sh)

## Solution: C++
```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hmap;

        for(const string& str: strs){
            string key = str;
            sort(key.begin(), key.end());
            hmap[key].push_back(str);
        }

        vector<vector<string>> output;
        output.reserve(hmap.size());
        for(auto& e: hmap){
            output.push_back(e.second);
        }

        return output;
    }
};
```
- **Time Complexity**: O(n*klogk)
- **Space Complexity**: O(n*k)

## Solution: C++
```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hmap;

        for(const string& str: strs){
            vector<int> cnt(26, 0);
            for(char ch: str){
                cnt[ch-'a']++;
            }
            string hash = "";
            for(int i=0; i<26; i++){
                hash += to_string(cnt[i]) + '#';
            }
            hmap[hash].push_back(str);
        }

        vector<vector<string>> output;
        output.reserve(hmap.size());
        for(auto& e: hmap){
            output.push_back(e.second);
        }

        return output;
    }
};
```
- **Time Complexity**: O(n*k)
- **Space Complexity**: O(n*k)
