class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def sumHelper(i,currSum):
            nonlocal nums
            # print (currSum)
            if currSum==0:
                return True
            if currSum < 0 or i < 0 :
                return False
            
            if sumHelper(i-1,currSum) or sumHelper(i-1,currSum-nums[i]):
                return True
            return False
        
        return sumHelper(len(nums)-1,sum(nums)//2) if sum(nums)%2==0 else False