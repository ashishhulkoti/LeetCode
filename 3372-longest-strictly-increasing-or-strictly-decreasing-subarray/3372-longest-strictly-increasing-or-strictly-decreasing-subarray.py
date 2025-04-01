class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr_linc,curr_ldec,lonest_inc,lonest_dec=1,1,1,1

        for i in range(1,len(nums)):    
            if nums[i]>nums[i-1]:
                curr_linc+=1
                if curr_ldec>lonest_dec:
                    lonest_dec=curr_ldec
                curr_ldec=1
            elif nums[i]<nums[i-1]:
                curr_ldec+=1
                if curr_linc>lonest_inc:
                    lonest_inc=curr_linc
                curr_linc=1
            else:
                if curr_ldec>lonest_dec:
                    lonest_dec=curr_ldec
                curr_ldec=1
                if curr_linc>lonest_inc:
                    lonest_inc=curr_linc
                curr_linc=1

        lonest_inc=max(lonest_inc,curr_linc)
        lonest_dec=max(lonest_dec,curr_ldec)
        return max(lonest_inc,lonest_dec)
