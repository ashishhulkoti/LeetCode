class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_string = [str(num) for num in nums]

        nums_string.sort(key=lambda a : a * 10, reverse=True)

        if nums_string[0] == "0":
            return "0"
        
        return ''.join(nums_string)