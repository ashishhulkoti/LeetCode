class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        stonesPos = set(stones)
        memo = {}
        def cross(i, k):
            if i not in stonesPos:
                return False
            if (i,k) in memo:
                return memo[(i,k)]
            if i == stones[-1]:
                # memo[(i,k)] = True
                return True
            
            c1 = False
            if k-1 > 0 and cross(i + k - 1, k - 1):
                # memo[(i,k)] = True
                return True
            c2 = False
            if k > 0 and cross(i + k, k):
                # memo[(i,k)] =  True
                return True
            c3 = False
            if cross(i + k + 1, k+1):
                return True
            memo[(i,k)] = False
            return False
        
        return cross(0,0)