# 217. Contains Duplicate - [link](https://leetcode.com/problems/contains-duplicate/?envType=problem-list-v2&envId=vsm9u0sh&)

## Solution: C++
```cpp
class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_map<int, int> hmap;
        for (int e : nums) {
            hmap[e]++;
            if (hmap[e] > 1) return true;
        }
        return false;
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

## Solution: C++
```cpp
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
- **Time Complexity**: O(nlogn)
- **Space Complexity**: O(1)
