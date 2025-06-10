class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        dp = [[[-1 for _ in range(51)] for __ in range(51)] for ___ in range(len(nums))]
        def countPairs(idx,x,y):
            if idx == (len(nums) - 1):
                return 1
            if dp[idx][x][y] != -1:
                return dp[idx][x][y]
            count = 0

            nextNum = nums[idx+1]

            for i in range(nextNum+1):
                if x <= i and y >= (nextNum - i):
                    count += countPairs(idx+1,i,(nextNum - i))
            
            dp[idx][x][y] = count
            return count
        
        count1 = 0

        nNum = nums[0]

        for j in range(nNum+1):
            if float("-inf") <= j and float("inf") >= (nNum - j):
                count1 += countPairs(0,j,(nNum - j))
        
        return count1%(10**9 + 7)


# class Solution:
#     def countOfPairs(self, nums: List[int]) -> int:
        
#         @cache
#         def countPairs(idx,x,y):
#             # print(idx,x,y)
#             if idx == (len(nums) - 1):
#                 return 1
            
#             count = 0

#             nextNum = nums[idx+1]

#             for i in range(nextNum+1):
#                 if x <= i and y >= (nextNum - i):
#                     count += countPairs(idx+1,i,(nextNum - i))
#             return count
        
#         return countPairs(-1,float("-inf"),float("inf"))%(10**9 + 7)