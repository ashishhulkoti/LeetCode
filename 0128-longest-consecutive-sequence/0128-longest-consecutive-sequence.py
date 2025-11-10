class Solution:
    
    def findRange(self, x, seq):
        highRange = x+1

        while highRange in seq:
            highRange+=1
        return highRange-x

    
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        maxSeq = 0
        for number in seq:
            if number-1 not in seq:
                maxSeq = max(maxSeq, self.findRange(number, seq))
        return maxSeq
        