class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0,float("-inf"))
        nums.append(float("-inf"))
        left,right=1,len(nums)

        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid-1
            if nums[mid]<nums[mid-1]:
                right=mid-1
            else:
                left=mid+1
        return mid