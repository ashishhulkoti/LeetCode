class Solution:
    def rob(self, nums: List[int]) -> int:
        highest=0
        @cache
        def helpRob(i,amt):
            nonlocal nums,highest
            if i>=len(nums):
                if amt>highest:
                    highest=amt
                return
            helpRob(i+1,amt)
            helpRob(i+2,amt+nums[i])

        helpRob(0,0)
        return highest

            
            

            