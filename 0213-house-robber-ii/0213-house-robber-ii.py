class Solution:
    def rob(self, nums: List[int]) -> int:
        withOne = nums[:-1]
        withLast = nums[1:]
        maxM = 0
        dp = [0] * len(withOne)
        if len(nums) <=2:
            return max(nums)
        for array in [withOne, withLast]:
            dp[0] = array[0]
            dp[1] = max(array[0], array[1])

            for i in range(2,len(array)):
                dp[i] = max(dp[i-1],dp[i-2]+array[i])
            
            maxM = max(dp[-1], maxM)
        return maxM
