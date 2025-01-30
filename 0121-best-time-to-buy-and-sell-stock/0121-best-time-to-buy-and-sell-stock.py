class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell=0,1
        profit=0
        while sell<len(prices):
            curr=prices[sell]-prices[buy]
            if prices[buy] < prices[sell]:
                if curr > profit:
                    profit=curr
            else:
                buy=sell  
            sell+=1
        return profit