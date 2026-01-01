# 📚 200. Number of Islands - [leetcode](https://leetcode.com/problems/number-of-islands/?envType=problem-list-v2&envId=vsm9u0sh&)

## 📝 Problem Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.  

## 📖 Solution: C++
```cpp
class Solution {
    int M, N;
    void discoverIsland(vector<vector<char>>& grid, int i, int j){
        grid[i][j] = '-';
        if(i > 0 && grid[i-1][j] == '1')
            discoverIsland(grid, i-1, j);
        if(i < M-1 && grid[i+1][j] == '1')
            discoverIsland(grid, i+1, j);
        if(j > 0 && grid[i][j-1] == '1')
            discoverIsland(grid, i, j-1);
        if(j < N-1 && grid[i][j+1] == '1')
            discoverIsland(grid, i, j+1);
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        M = grid.size();
        N = grid[0].size();

        int result = 0;
        for(int i=0; i<M; i++)
            for(int j=0; j<N; j++)
                if(grid[i][j] == '1'){
                    result++;
                    discoverIsland(grid, i, j);
                }
        
        return result;
    }
};
```
- **Time Complexity**: $O(M \cdot N)$
- **Space Complexity**: $O(1)$
### 📝 Reviewer Notes

- The solution uses a **Depth First Search (DFS)** approach to traverse and mark all connected land cells ('1') as visited ('-').
- **In-place modification**: By changing '1' to '-', we avoid using an auxiliary `visited` matrix, keeping the space complexity focused on the recursion stack.
- **Recursive Stack**: In the worst case (a grid filled with land), the recursion depth can reach $M \times N$, which defines the space complexity.
- **Efficiency**: Each cell is visited at most once, ensuring an optimal linear time complexity relative to the number of cells in the grid.
