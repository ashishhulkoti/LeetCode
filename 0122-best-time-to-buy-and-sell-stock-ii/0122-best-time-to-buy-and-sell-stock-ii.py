class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices)==1:
        #     return 0
        # l,r=0,1
        profit=0
        for r in range(1,len(prices)):
            diff=prices[r]-prices[r-1]
            if diff>0:
                profit+=diff
        return profit