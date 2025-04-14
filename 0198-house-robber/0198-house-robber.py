class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helpRob(i):
            if i>=len(nums):
                return 0
            return max(helpRob(i+1),helpRob(i+2)+nums[i])
        return helpRob(0)

            
            

            