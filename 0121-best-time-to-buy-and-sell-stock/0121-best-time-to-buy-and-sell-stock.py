class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 1
        stockMinPrice = prices[0] 
        while i < len(prices):
            if prices[i] > stockMinPrice:
                maxProfit = max(maxProfit, prices[i]-stockMinPrice)
            else:
                stockMinPrice = prices[i]
            i+=1
        return maxProfit

