class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        max_sum=nums[0]
        i=1
        temp_sum=max_sum
        while i<len(nums):
            if nums[i]>nums[i-1]:
                temp_sum+=nums[i]
            else:
                if temp_sum>max_sum:
                    max_sum=temp_sum
                temp_sum=nums[i]
            i+=1
        if temp_sum>max_sum:
            max_sum=temp_sum
        return max_sum


