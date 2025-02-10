class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        l=0
        r=len(nums)-1

        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]>=target:
                r=mid-1
            else:
                l=mid+1
        # print(l)
        if l==len(nums) or nums[l]!=target:
            return [-1,-1]
        start=l
        l=start
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid-1
        end=r
        return [start,end]