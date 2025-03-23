class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left,right=0,0
        count=0
        product=1
        if k<=1:
            return 0
        while right<len(nums):
            if product*nums[right]<k:
                count+=right-left+1
                product*=nums[right]
                right+=1
            else:
                product=product/nums[left]
                left+=1
                if left>=right:
                    product=1
                    right=left

        return count
        