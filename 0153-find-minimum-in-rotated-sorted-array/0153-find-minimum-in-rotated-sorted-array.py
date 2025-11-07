class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l<r:
            mid = l + (r-l)//2
            # print(nums[l], nums[mid], nums[r])
            if nums[l] <= nums[r] and nums[l] <= nums[mid]:
                return nums[l]
            elif nums[mid] <= nums[l] and nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
        