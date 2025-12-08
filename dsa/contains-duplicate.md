# 
##### [LINK](https://leetcode.com/problems/contains-duplicate?envType=problem-list-v2&envId=vsm9u0sh)

```
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for(int i=0; i<nums.size()-1; i++){
            if(nums[i] == nums[i+1]) return true;
        }
        return false;
    }
};
```