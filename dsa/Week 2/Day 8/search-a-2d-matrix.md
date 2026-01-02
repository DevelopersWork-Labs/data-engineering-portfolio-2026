# 📚 74. Search a 2D Matrix - [leetcode](https://leetcode.com/problems/search-a-2d-matrix/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write an algorithm with $O(\log(m \cdot n))$ runtime complexity.

## 📖 Solution: C++
```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size(), n=matrix[0].size();
        int i=0, j=0;
        while(i < m-1 && target >= matrix[i+1][j]) i++;
        while(j < n-1 && target > matrix[i][j]) j++;
        return matrix[i][j] == target;
    }
};
```
- **Time Complexity**: $O(m + n)$
- **Space Complexity**: $O(1)$
### 📝 Reviewer Notes

- The current implementation uses linear scans for rows and columns, resulting in $O(m + n)$ time complexity, which does not meet the $O(\log(m \cdot n))$ requirement.
- To achieve the required complexity, treat the 2D matrix as a single sorted 1D array of size $m \times n$ and perform binary search.
- The mapping from a 1D index `mid` to 2D coordinates is `row = mid / n` and `col = mid % n`.

## 📖 Solution: C++
```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size(), n=matrix[0].size();
        int l=0, h=m*n-1;
        int i=0,j=0,mid;
        
        while(l <= h){
            mid = (l+h)/2;
            i = mid/n;
            j = mid%n;
            if(matrix[i][j] == target) return true;
            if(matrix[i][j] < target) l = mid+1;
            else h = mid-1;
        }

        return matrix[i][j] == target;
    }
};
```
- **Time Complexity**: $O(\log(m \cdot n))$
- **Space Complexity**: $O(1)$
### 📝 Reviewer Notes

- This implementation correctly achieves the $O(\log(m \cdot n))$ time complexity by treating the matrix as a virtual 1D sorted array.
- The coordinate mapping `i = mid / n` and `j = mid % n` allows for standard binary search logic without extra space.
- To prevent potential integer overflow in other contexts, `mid = l + (h - l) / 2` is a safer alternative to `(l + h) / 2`.
- Since the target is returned immediately upon discovery within the loop, the final statement can be simplified to `return false;`.
