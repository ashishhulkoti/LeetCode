import math
class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        x = n
        while n!=0:
            n = abs(n - 2**(int(round(math.log2(n)))))
            count+=1
        return count