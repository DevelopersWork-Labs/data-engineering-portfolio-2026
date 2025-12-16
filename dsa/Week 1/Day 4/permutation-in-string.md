# 567. Permutation in String - [link](https://leetcode.com/problems/permutation-in-string/?envType=problem-list-v2&envId=vsm9u0sh&) 

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
                if(count(freq.begin(), freq.end(), 0) == 256)
                    return true;
            }
            while(i<j && freq[ch] < 0){
                freq[s2[i]]++;
                i++;
            }
            if(count(freq.begin(), freq.end(), 0) == 256)
                return true;
        }

        return false;
    }
};
```