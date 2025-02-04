class Solution:
    def dfs(self, grid, i, j):
        if (i < 0) or (j < 0) or (i > len(grid)-1) or (j > len(grid[0])-1) or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
        return

    def numIslands(self, grid) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    result += 1
        return result
