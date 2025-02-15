class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        checker=1
        while i<len(nums) and nums[i]<=0:
            i+=1
        if i==len(nums) or nums[i]!=1:
            return 1
        i+=1
        checker+=1
        prev=i-1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                i+=1
                continue
            
            if nums[i]==nums[prev]+1:
                checker+=1
                prev=i
                i+=1
            else:
                return checker
        return checker