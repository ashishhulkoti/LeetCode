class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = prices[0]
        max_profit = 0

        i = 1

        while i<len(prices):
            if prices[i] < high:
                max_profit += high - low
                low = prices[i]
                high = prices[i]
            else:
                high = prices[i]
            i+=1
        
        return max_profit + (high - low)