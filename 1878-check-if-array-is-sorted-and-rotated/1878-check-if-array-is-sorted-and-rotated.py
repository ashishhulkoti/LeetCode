class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        i=1
        while i<len(nums):
            if nums[i]<nums[i-1]:
                break
            i+=1
        if i==len(nums):
            return True
        while i<len(nums)-1:
            if nums[i]>nums[i+1]:
                return False
            i+=1
        if nums[len(nums)-1]>nums[0]:
            return False
        return True