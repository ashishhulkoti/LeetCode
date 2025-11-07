import math
class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        x = n
        # print(math.log2(10))
        # return 0
        while n!=0:
            n = abs(n - 2**(int(round(math.log2(n)))))
            # print(n)
            count+=1
        return count