class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        unique = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    unique.add(self.dfs(grid, i, j, "s"))
        return len(unique)
                    
    def dfs(self, grid, i, j, pattern):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return ""
        
        grid[i][j] = -1
        return pattern + self.dfs(grid, i-1, j, "U") + "D" + self.dfs(grid, i+1, j, "D") + "U" + self.dfs(grid, i, j-1, "L") + "R" + self.dfs(grid, i, j+1, "R") + "L"
