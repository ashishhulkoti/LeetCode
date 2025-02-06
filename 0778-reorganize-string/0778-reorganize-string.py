from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s)==1:
            return s
        c_count=Counter(s)
        if c_count.most_common()[0][1] > (len(s)+1)//2:
            return ""
        ans=[""]*len(s)
        i=0
        for c,n in c_count.most_common():
            while n>0:
                ans[i]=c
                n-=1
                i+=2
                if i>=len(ans):
                    i=1
        return ''.join(ans)

        