class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        i = 0
        while i<len(nums):
            if nums[i] == 0:
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                l+=1
            i+=1
        r = len(nums) - 1
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == 2:
                temp = nums[r]
                nums[r] = nums[i]
                nums[i] = temp
                r-=1
            i-=1
