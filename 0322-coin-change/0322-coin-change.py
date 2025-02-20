class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp=[float("inf")] * (amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            minn=float("inf")
            for coin in coins:
                diff=i-coin
                if diff<0:
                    break
                minn=min(minn,1+dp[diff])
            dp[i]=minn
        if dp[amount]<float("inf"):
            return dp[amount]
        return -1
                