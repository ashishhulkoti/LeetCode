class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zero_count=0
        zero_ind={}
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
                zero_ind[0]=i
                continue
            product*=nums[i]
            
        if zero_count>=2:
            return [0]*len(nums)
        ans=[]
        if zero_count==1:
            ans=[0]*len(nums)
            ans[zero_ind[0]]=product
            return ans
        for i in range(len(nums)):
            ans.append(product//nums[i])
        return ans