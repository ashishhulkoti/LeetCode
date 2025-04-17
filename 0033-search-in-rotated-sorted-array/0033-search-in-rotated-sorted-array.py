class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0,len(nums)-1

        while left<right:
            mid = (left + right) // 2    
            if nums[mid]<=nums[right]:
                right=mid
            else:
                left=mid+1
        
        pivot=left

        if target == nums[pivot]:
            return pivot

        left,right=0,len(nums)-1        
        
        if pivot == len(nums)-1:
            right=pivot-1
        elif pivot==0:
            pass
        elif target <= nums[pivot-1] and target>=nums[left]:
            right=pivot-1
        else:
            left=pivot+1
        
        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return mid
            
            if target < nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1
        