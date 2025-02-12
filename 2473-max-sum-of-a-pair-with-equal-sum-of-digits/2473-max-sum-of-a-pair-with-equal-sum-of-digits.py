class Solution:
    def sum_digit(self,n):
        sum=0
        while n>0:
            sum+=n%10
            n=n//10
        return sum
    def maximumSum(self, nums: List[int]) -> int:
        max_sum=-1
        digitsumdict={}
        # num_dict={}
        for i in range(len(nums)):
            digit_sum=self.sum_digit(nums[i])
            # print(digit_sum)
            if digit_sum in digitsumdict:
                tmp=digitsumdict[digit_sum]+nums[i]
                if tmp>max_sum:
                    max_sum=tmp
                if nums[i]>digitsumdict[digit_sum]:
                    digitsumdict[digit_sum]=nums[i]
            else:
                digitsumdict[digit_sum]=nums[i]
        return max_sum