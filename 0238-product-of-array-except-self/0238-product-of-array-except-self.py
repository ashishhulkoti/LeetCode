class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if len(nums)==2:
        #     return [nums[1],nums[0]]
        prod_l,prod_r=1,1
        ans=[1]*len(nums)

        l,r=0,len(nums)-1

        while r>=0:
            ans[l]*=prod_l
            ans[r]*=prod_r
            prod_l*=nums[l]        
            prod_r*=nums[r]
            l+=1
            r-=1
        return ans