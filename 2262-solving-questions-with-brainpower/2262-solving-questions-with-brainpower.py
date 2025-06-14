class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        

        dp = [0] * (len(questions)+1)
        for i in range(len(questions)-1,-1,-1):
            takeIdx = min(i + 1 + questions[i][1], len(dp)-1)
            dp[i] = max(questions[i][0] + dp[takeIdx], dp[i+1])
        return dp[0]