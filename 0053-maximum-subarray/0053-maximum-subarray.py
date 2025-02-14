class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=0
        max_sum=float("-inf")
        highest=nums[0]
        for n in nums:
            curr_sum+=n
            if curr_sum>max_sum:
                max_sum=curr_sum
            if curr_sum<0:
                curr_sum=0
            # else:
            # if n>highest:
            #     highest=n
        return max_sum
        # return max(max_sum,highest)
