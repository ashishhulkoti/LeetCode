class Solution:
    def isPalindrome(self, x: int) -> bool:
        dum=str(x)
        i=0
        j=len(dum)-1
        while i<=j:
            if not dum[i]==dum[j]:
                return False
            i+=1
            j-=1
        return True