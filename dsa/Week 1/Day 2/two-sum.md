# 📚 1. Two Sum - [link](https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## 📖 Solution: C++
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hmap;

        for(int i=0; i<nums.size(); i++){
            if(hmap.find(nums[i]) != hmap.end()){
                return vector<int>{hmap[nums[i]], i};
            }
            int v = target - nums[i];
            hmap[v] = i;
        }
        return vector<int>{-1, -1};
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
### 📝 Reviewer Notes

This is a standard and efficient solution for the Two Sum problem.

- **Approach**: The solution correctly uses a hash map (`unordered_map`) to store the `complement` needed for each number encountered so far, along with its index. This allows for O(1) average time lookups.
- **Correctness**: The logic is sound. For each number `nums[i]`, it first checks if `nums[i]` itself is a complement of a previously seen number (i.e., if `nums[i]` is a key in the map). If found, the pair is identified. If not, the `target - nums[i]` (the complement of `nums[i]`) is stored in the map with `i` as its value, anticipating that a future number might be this complement.
- **Edge Cases**: The problem statement guarantees exactly one solution, so there's no need to handle cases with multiple solutions or no solutions, but the `return {-1, -1}` handles the theoretical case where no pair is found (though unreachable given problem constraints).
- **Readability**: The code is clear and easy to understand.
- **Optimality**: Both time and space complexities are optimal for this problem using a hash-based approach.
