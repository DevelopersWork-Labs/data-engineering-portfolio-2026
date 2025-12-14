# 📚 347. Top K Frequent Elements - [link](https://leetcode.com/problems/top-k-frequent-elements/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## 📖 Solution: C++
```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> freq;
        freq.reserve(n);
        for(int e: nums){
            freq[e]++;
        }

        map<int, vector<int>, greater<int>> freq2;
        for(const auto& e: freq){
            freq2[e.second].push_back(e.first);
        }

        vector<int> result(k);
        for(const auto& e: freq2){
            if(k <= 0) break;
            for(int i: e.second){
                if(k <= 0) break;
                result[--k] = i;
            }
        }

        return result;
    }
};
```
- **Time Complexity**: O(nlogn)
- **Space Complexity**: O(n)
### 📝 Reviewer Notes

The solution correctly identifies the frequencies of elements and then sorts them to find the top `k`. However, the use of `std::map<int, vector<int>, greater<int>>` for sorting frequencies leads to a time complexity of `O(N log N)` in the worst case, where `N` is the number of elements and `M` is the number of unique elements (as `std::map` operations are `log M`).

More optimal approaches for this problem typically involve:
1.  **Min-Priority Queue**: After counting frequencies, iterate through the frequency map and maintain a min-priority queue of size `k`. This would result in `O(N log K)` time complexity.
2.  **Bucket Sort**: Create an array of lists (buckets) where the index represents the frequency. Populate these buckets with numbers, then iterate from the highest frequency bucket downwards until `k` elements are collected. This approach can achieve `O(N)` time complexity.

While the current solution is correct, considering these alternatives could lead to a more performant solution for larger inputs.

## 📖 Solution: C++
```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> freq;
        freq.reserve(n);
        for(int e: nums){
            freq[e]++;
        }

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> min_queue;
        for(const auto& e: freq){
            min_queue.push({e.second, e.first});
            while(min_queue.size() > k) min_queue.pop();
        }

        vector<int> result;
        result.reserve(k);
        for(int i=0; i<k; i++){
            result.push_back(min_queue.top().second);
            min_queue.pop();
        }

        return result;
    }
};
```
- **Time Complexity**: O(nlogk)
- **Space Complexity**: O(n)
### 📝 Reviewer Notes

This solution correctly implements the min-priority queue approach.
- **Time Complexity**: O(N log K) due to iterating through `N` elements and performing `log K` operations for the priority queue.
- **Space Complexity**: O(N) for the frequency map and O(K) for the priority queue, resulting in O(N) overall.
- The use of `reserve` for the `unordered_map` and `vector` is a good optimization.
- The logic for maintaining a min-priority queue of size `k` is sound.
