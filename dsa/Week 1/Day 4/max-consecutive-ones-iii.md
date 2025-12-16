# 1004. Max Consecutive Ones III - [link](https://leetcode.com/problems/max-consecutive-ones-iii/?envType=problem-list-v2&envId=vsm9u0sh&)

```cpp
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size();
        int i=0, j=0, result = 0, flp = 0;

        while(i < n && j < n){
            while(j < n){
                if(nums[j] == 0){
                    if(flp >= k) break;
                    else flp++;
                }
                j++;
            }
            result = max(result, j - i);
            while(i < j && flp >= k){
                if(nums[i] == 0) flp--;
                i++;
            }
            if(i < n && i == j && nums[i] == 0 && k == 0){
                i++;
                j++;
            }
        }

        return result;
    }
};
```