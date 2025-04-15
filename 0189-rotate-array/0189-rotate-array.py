class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seen=set()
        n = len(nums)
        prevNum = nums[0]
        i=k%n
        lseen=len(seen)
        count=0
        while lseen < n :
            count+=1
            if i in seen:
                prevNum = nums[(i+1)%n]
                i = (i+k+1)%n
                continue
            seen.add(i)
            lseen+=1
            tmp=nums[i]
            nums[i] = prevNum
            prevNum = tmp
            i = (i + k) % n
        return 
