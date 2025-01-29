class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        first_part,second_part="",""
        longest_length=0
        k=0
        str_size=len(s)
        
        

        while (k+longest_length) < str_size:
            temp=longest_length
            while (k+temp) < str_size:
                i=k
                j=k+temp
                dum_length=0
                dum=""
                while i<j:
                    if s[i]==s[j]:
                        first_part=first_part + s[i]
                        second_part=s[j] + second_part
                    else:
                        break
                    i+=1
                    j-=1

                if i==j:
                    dum=first_part+s[i]+second_part
                    dum_length=len(dum)
                elif i>j:
                    dum=first_part+second_part
                    dum_length=len(dum)
                if dum_length>longest_length:
                    longest_length=dum_length
                    longest=dum
                temp+=1
                first_part=""
                second_part=""
            k+=1
        return longest
        
            
                