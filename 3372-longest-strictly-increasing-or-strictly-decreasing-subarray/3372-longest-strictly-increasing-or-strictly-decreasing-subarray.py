class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        longest_i=0
        longest_d=0
        l=0
        r=1
        while l<len(nums) and r<len(nums):
            if l<r:
                if nums[r]>nums[r-1]:
                    r+=1
                else:
                    if longest_i<(r-l):
                        longest_i=r-l
                    if nums[r]==nums[r-1]:
                        l=r+1
                    else:
                        l=r
                        r-=1
            else:
                if nums[l]<nums[l-1]:
                    l+=1
                else:
                    if longest_d<(l-r):
                        longest_d=l-r
                    if nums[l]==nums[l-1]:
                        r=l+1
                    else:
                        r=l
                        l-=1
        if l<r and longest_i<(r-l):
            longest_i=r-l
        elif r<l and longest_d<(l-r):
            longest_d=l-r

        if longest_i < longest_d:
            return longest_d
        else:
            return longest_i

