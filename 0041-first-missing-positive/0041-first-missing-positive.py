class Solution:
    def swap(self, nums, i, j):
        if nums[i] == nums[j]:
            return False
        nums[i] , nums[j] = nums[j], nums[i]
        return True
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        while i<len(nums):
            if nums[i]>=1 and nums[i]<len(nums) and nums[i]!=(i+1):
                if not self.swap(nums, i, nums[i]-1):
                    i+=1
            else:
                i+=1

        for i, number in enumerate(nums):
            if number != (i+1):
                return i+1
        return len(nums) + 1
            