class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]
        if n==0:
            return dp
        # dp.append(1)
        prev_power=1
        next_power=2
        for i in range(1,n+1):
            if i==next_power:
                dp.append(1)
                prev_power=next_power
                next_power*=2
            else:
                dp.append(1+dp[i%prev_power])
        return dp 