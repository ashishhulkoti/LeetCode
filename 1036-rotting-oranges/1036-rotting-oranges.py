class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dp = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]

        original_rotten = set()

        def bfsHelper(currQ):
            nonlocal dp, grid, original_rotten
            t = 0
            while currQ:
                orngr, orngc, orngt = currQ.pop(0)
                if grid[orngr][orngc] == 0:
                    continue
                if grid[orngr][orngc] == 2 and (orngr, orngc) not in original_rotten:
                    original_rotten.add((orngr, orngc))
                    bfsHelper([(orngr,orngc,0)])    

                if orngt < dp[orngr][orngc]:
                    dp[orngr][orngc] = orngt
                else:
                    continue
                for r,c in [(0,1),(1,0),(-1,0),(0,-1)]:
                    if 0 <= orngr+ r < len(grid) and 0 <= orngc+ c < len(grid[0]):
                            currQ.append((orngr + r,orngc + c, orngt + 1))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 2:
                    if (i,j) in original_rotten:
                        continue
                    original_rotten.add((i,j))
                    bfsHelper([(i,j,0)])
        maxT=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if dp[i][j] == float("inf"):
                        return -1
                    if dp[i][j]>maxT:
                        maxT=dp[i][j]
        return maxT