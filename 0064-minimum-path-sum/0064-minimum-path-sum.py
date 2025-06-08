class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        # dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num = grid[i][j]
                grid[i][j] = float("inf")
                if i == 0 and j == 0:
                    grid[i][j] = num
                if i>0:
                    grid[i][j] = min(grid[i][j], num + grid[i-1][j])
                if j>0:
                    grid[i][j] = min(grid[i][j], num + grid[i][j-1])
                
        return grid[-1][-1]