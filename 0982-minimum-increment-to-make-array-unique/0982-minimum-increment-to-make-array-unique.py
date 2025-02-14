class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev=nums[0]
        count=0
        for i in range(1,len(nums)):
            if nums[i]<=prev:
                req=prev-nums[i]+1
                nums[i]=prev+1
                count+=req
            prev=nums[i]
        return count