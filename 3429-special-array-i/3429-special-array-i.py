class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        # i,j=0,len(nums)-1
        # if len(nums)%2==0:
        #     if (nums[i]+nums[j])%2==1:
        #         j-=1
        #     else:
        #         return False
        i=0
        while i<=len(nums)-2:
            if (nums[i]+nums[i+1])%2==0:
                return False
            i+=1
        return True
