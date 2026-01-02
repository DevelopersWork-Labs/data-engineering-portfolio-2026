# 📚 704. Binary Search - [leetcode](https://leetcode.com/problems/binary-search/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return -1.

You must write an algorithm with $O(\log n)$ runtime complexity.

## 📖 Solution: C++
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0, h=nums.size()-1;
        
        int m;
        while(l < h){
            m = (l+h)/2;
            if(nums[m] == target) return m;
            if(nums[m] < target) l=m+1;
            else h=m-1;
        }

        return nums[l] == target ? l : -1;
    }
};
```
- **Time Complexity**: $O(\log n)$
- **Space Complexity**: $O(1)$
### 📝 Reviewer Notes

- **Overflow Prevention**: The calculation `m = (l + h) / 2` is susceptible to integer overflow if the sum of `l` and `h` exceeds the maximum value of `int`. A safer alternative is `m = l + (h - l) / 2`.
- **Empty Input**: The code does not explicitly handle the case where `nums` is empty. If `nums.size()` is 0, `h` becomes `-1` (or a large value if `size_t` underflow occurs), and `nums[l]` will result in an out-of-bounds access.
- **Loop Logic**: The `while(l < h)` condition combined with the final ternary check is a valid variation, but ensure the input size is at least 1 to avoid runtime errors.

