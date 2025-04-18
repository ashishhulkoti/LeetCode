class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=0
        max_sum=nums[0]
        highest=nums[0]
        for n in nums:
            curr_sum+=n
            if curr_sum<0:
                curr_sum=0
            else:
                if curr_sum>max_sum:
                    max_sum=curr_sum
            if n>highest:
                highest=n
        if max_sum>=highest:
            return max_sum
        else:
            return highest
