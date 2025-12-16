# 📚 1004. Max Consecutive Ones III - [link](https://leetcode.com/problems/max-consecutive-ones-iii/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

You are given a binary array `nums` and an integer `k`. The task is to find the maximum number of consecutive 1's in the array after flipping at most `k` 0's.

## 📖 Solution: C++
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
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
### 📝 Reviewer Notes

- The solution uses a sliding window approach to find the maximum number of consecutive 1's in the array after flipping at most `k` 0's.
- The `while` loop iterates through the array, and the inner `while` loop extends the window by moving the right pointer `j` to the right until a 0 is encountered.
- The `result` variable is updated with the maximum length of the window found so far.
- The `while` loop then contracts the window by moving the left pointer `i` to the right until the number of flips is less than or equal to `k`.
- The `if` statement handles the case where the left pointer is equal to the right pointer and the current element is 0, and `k` is 0.
- The time complexity is O(n) as the `while` loop iterates through the array only once.
- The space complexity is O(1) as the solution only uses a few constant variables.
