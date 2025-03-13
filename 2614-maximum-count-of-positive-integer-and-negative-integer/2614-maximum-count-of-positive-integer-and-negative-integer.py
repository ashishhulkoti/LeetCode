class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos,neg,zeroes=0,0,0
        for x in nums:
            if x==0:
                zeroes+=1
            elif x<0:
                neg+=1
            else:
                break
        pos=len(nums)-zeroes-neg
        return max(pos,neg)