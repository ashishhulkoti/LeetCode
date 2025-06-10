class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        memo = {}
        # @cache
        def countPairs(idx,x,y):
            if (idx,x,y) in memo:
                return memo[(idx,x,y)]
            if idx == (len(nums) - 1):
                return 1
            
            count = 0

            nextNum = nums[idx+1]

            for i in range(nextNum+1):
                if x <= i and y >= (nextNum - i):
                    count += countPairs(idx+1,i,(nextNum - i))
            memo[(idx,x,y)] = count
            return count
        
        return countPairs(-1,float("-inf"),float("inf"))%(10**9 + 7)