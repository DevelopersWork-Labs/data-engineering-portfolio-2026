# 📚 121. Best Time to Buy and Sell Stock - [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## 📖 Solution: C++
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mx = 0, curr = 0;
        int n = prices.size();

        int i = 0, j = 1;
        while(i < n && j < n){
            j = i+1;
            while(j < n){
                curr = prices[j] - prices[i];
                if(curr > mx){
                    mx = curr;
                }
                if(curr < 0) break;
                j++;
            }
            i = j;
        }

        return mx;
    }
};
```
- **Time Complexity**: O(n^2)
- **Space Complexity**: O(1)
### 📝 Reviewer Notes

- The initial solution attempts to find the maximum profit but includes logical errors that prevent it from correctly identifying the optimal buy/sell days.
- The `if(curr < 0) break;` condition prematurely exits the inner loop. A negative profit at `prices[j]` should not stop the search for a higher selling price relative to `prices[i]`, nor does it correctly identify `prices[j]` as a potential new buying point.
- The `i = j;` update in the outer loop causes `i` to skip potential buying days, leading to incorrect results, especially in cases where the price dips before rising again.
- Despite the intention, the nested loop structure results in a time complexity of O(n^2) in the worst-case scenario, as `i` and `j` do not always advance optimally.
- A more efficient approach typically involves a single pass to track the minimum price seen so far and continuously update the maximum profit.

## 📖 Solution: C++
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int mx = 0, curr, min_p = prices[0];
        
        for(int i=1; i<n; i++){
            if(prices[i] < min_p){
                min_p = prices[i];
                continue;
            }
            mx = max(mx, prices[i] - min_p);
        }

        return mx;
    }
};
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
### 📝 Reviewer Notes

- This optimized solution correctly identifies the maximum profit by iterating through the prices array only once.
- It efficiently tracks the minimum price encountered so far (`min_p`) and updates the maximum profit (`mx`) based on the difference between the current price and `min_p`.
- The logic correctly handles cases where a new minimum price is found, effectively resetting the potential buying point.
- The time complexity is O(n) as it involves a single pass through the array.
- The space complexity is O(1) as it only uses a few constant variables, making it highly efficient.

