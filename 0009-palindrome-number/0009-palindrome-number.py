class Solution:
    def isPalindrome(self, x: int) -> bool:
        dum=0
        origin=x
        if x<0 or (x!=0 and x%10==0):
            return False
        while x!=0:
            dum=dum*10+x%10
            x=x//10
        return origin==dum