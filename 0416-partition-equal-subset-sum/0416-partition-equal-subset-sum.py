class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        flag=False
        @cache
        def sumHelper(i,currSum):
            nonlocal nums
            nonlocal flag
            # print (currSum)
            if currSum==0:
                return True
            if currSum < 0 or i < 0 :
                return False
            
            if not flag and sumHelper(i-1,currSum) or sumHelper(i-1,currSum-nums[i]):
                flag=True
                return True
            return False
        
        return sumHelper(len(nums)-1,sum(nums)//2) if sum(nums)%2==0 else False