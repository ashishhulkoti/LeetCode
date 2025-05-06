class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dp = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 2:
                    currQ = []
                    currQ.append((i,j,0))
                    t = 0

                    while currQ:
                        orngr, orngc, orngt = currQ.pop(0)
                        if grid[orngr][orngc] == 0:
                            continue
                        if orngt < dp[orngr][orngc]:
                            dp[orngr][orngc] = orngt
                        else:
                            continue
                        for r,c in [(0,1),(1,0),(-1,0),(0,-1)]:
                            if 0 <= orngr+ r < len(grid) and 0 <= orngc+ c < len(grid[0]):
                                    currQ.append((orngr + r,orngc + c, orngt + 1))
        maxT=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if dp[i][j] == float("inf"):
                        return -1
                    if dp[i][j]>maxT:
                        maxT=dp[i][j]
        return maxT
                    
                                
                                                    

