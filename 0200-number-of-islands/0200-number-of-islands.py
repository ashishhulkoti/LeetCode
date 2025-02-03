class Solution:
    
    def grid_dfs(self,grid,k,l):
        if k<0 or l<0 or l>=len(grid[0]) or k>=len(grid) or grid[k][l]!="1":
            return
        # if grid[k][l]!="1":
        #     return
        grid[k][l]="0"
        self.grid_dfs(grid,k-1,l)
        self.grid_dfs(grid,k,l-1)
        self.grid_dfs(grid,k+1,l)
        self.grid_dfs(grid,k,l+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.grid_dfs(grid,i,j)
                    count+=1
        return count
