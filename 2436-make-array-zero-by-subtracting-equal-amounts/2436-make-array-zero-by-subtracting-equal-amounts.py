class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        if nums[-1]==0:
            return 0
        for i in range(len(nums)-1):
            if nums[i]==0:
                continue
            if nums[i]!=nums[i+1]:
                count+=1
        return count