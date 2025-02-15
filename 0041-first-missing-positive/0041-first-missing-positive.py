class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        checker=1
        while i<len(nums) and nums[i]<=0:
            i+=1
        while i<(len(nums)-1):
            if nums[i]==nums[i+1]:
                i+=1
                continue
            if nums[i]==checker:
                checker+=1
                i+=1
            else:
                return checker
        if i==len(nums) or nums[i]!=checker:
            return checker
        return checker+1