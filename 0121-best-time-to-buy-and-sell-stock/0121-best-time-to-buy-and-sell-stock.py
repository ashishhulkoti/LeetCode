class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 1
        stockMinPrice = prices[0] 
        for currStock in prices:
            if currStock > stockMinPrice:
                maxProfit = max(maxProfit, currStock-stockMinPrice)
            else:
                stockMinPrice = currStock
            i+=1
        return maxProfit

