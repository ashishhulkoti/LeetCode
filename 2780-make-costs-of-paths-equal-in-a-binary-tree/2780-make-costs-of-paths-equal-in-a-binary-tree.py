class Solution:
    
    
    
    def minIncrements(self, n: int, cost: List[int]) -> int:
        
        count = 0
        cost.insert(0,0)
        def check(i):
            nonlocal count
            if i> n:
                return 0
            
            left = check(i*2)
            right = check(i*2+1)

            count+=abs(left-right)
            return cost[i] + max(left,right)
        check(1)

        return count        
