class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp=[[0]*len(s) for i in range(len(s))]
        s_size=len(s)
        longest_length=0
        longest=s[0]
        def check_palindrome(m,n):
            while m<=n:
                if s[m]!=s[n]:
                    return False
                m+=1
                n-=1
            return True
        
        if s_size==1:
            return s
        elif s_size==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        
        for i in range(s_size):
            if s_size-i<longest_length:
                break
            for j in range(s_size-1,i+longest_length-1,-1):
                if check_palindrome(i,j):
                    longest_length = j-i+1
                    longest=s[i:j+1]
                    print(i,j,longest)
                    break
        return longest