# 📚 238. Product of Array Except Self - [link](https://leetcode.com/problems/product-of-array-except-self/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

##  📖 Solution: C++
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();

        vector<int> p(n, 1), s(n, 1);
        p[0] = nums[0];
        s[n-1] = nums[n-1];
        for(int i=1; i<n; i++){
            p[i] *= p[i-1] * nums[i];
            s[n-i-1] *= s[n-i] * nums[n-i-1];
        }

        vector<int> result(n);
        result[0] = s[1];
        result[n-1] = p[n-2];
        for(int i=1; i<n-1; i++){
            result[i] = p[i-1] * s[i+1];
        }
        return result;
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
### 📝 Reviewer Notes

This solution correctly implements the product of array except self approach.
- **Time Complexity**: O(N) due to iterating through the array twice (once for prefix products and once for suffix products).
- **Space Complexity**: O(N) for storing the prefix and suffix products, resulting in O(N) overall.
- The logic for calculating prefix and suffix products is sound.

## Solution: C++
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1);

        for(int i=1; i<n; i++){
            result[i] = result[i-1] * nums[i-1];
        }

        int suffix = 1;
        for(int i=n-1; i>=0; i--){
            result[i] *= suffix;
            suffix *= nums[i];
        }
        return result;
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
### 📝 Reviewer Notes

This solution is an optimized version that achieves O(1) space complexity.
- **Time Complexity**: O(N) due to two passes over the array (one for prefix products, one for suffix products).
- **Space Complexity**: O(1) as it reuses the `result` array to store intermediate prefix products and then the final products, and only uses a single variable (`suffix`) for the backward pass. This effectively eliminates the need for separate prefix and suffix arrays.
- The logic is sound and efficiently combines the prefix and suffix product calculations into a single array.
