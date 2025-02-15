class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        # prev=nums[0]
        count=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                req=nums[i-1]-nums[i]+1
                nums[i]=nums[i-1]+1
                count+=req
            # prev=nums[i]
        return count