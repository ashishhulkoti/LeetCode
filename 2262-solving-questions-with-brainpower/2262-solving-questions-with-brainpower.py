class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        

        dp = [0] * (len(questions)+1)
        # def maxPoints(i):
        #     if i >= len(questions):
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = max(questions[i][0] + maxPoints(i + questions[i][1] + 1), maxPoints(i+1))
        #     return dp[i]

        # return maxPoints(0)
        for i in range(len(questions)-1,-1,-1):
            takeIdx = min(i + 1 + questions[i][1], len(dp)-1)
            dp[i] = max(questions[i][0] + dp[takeIdx], dp[i+1])
            # if takeIdx <= len(questions) - 1:
                # dp[i] = max(dp[i], dp[takeIdx] + questions[i][0])
        return dp[0]