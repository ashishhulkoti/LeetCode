class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        l,r=0,1
        profit=0
        while r<len(prices):
            if prices[r]<prices[r-1]:
                profit+=prices[r-1]-prices[l]
                l=r
                r+=1
            else:
                r+=1
        profit+=prices[r-1]-prices[l]
        return profit