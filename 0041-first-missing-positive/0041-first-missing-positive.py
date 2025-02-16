class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_dict=Counter(nums)
        last=1
        for i in range(1,len(nums_dict)+1):
            if i not in nums_dict:
                return i
            last+=1
        return last