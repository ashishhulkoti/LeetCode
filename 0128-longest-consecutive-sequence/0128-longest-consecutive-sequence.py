class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        nums.sort()
        count=1
        max=1
        # print(nums)
        for i in range(len(nums)-1):
            # print(nums[i],nums[i+1])
            if nums[i]==(nums[i+1]-1):
                count+=1
                if count>max:
                    max=count
            elif nums[i] < (nums[i+1]-1):
                count=1
            # print(i,i+1,count)
        return max