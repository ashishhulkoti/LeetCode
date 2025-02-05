class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sdict={}
        lp="("
        rp=")"
        sdict[lp]=[]
        sdict[rp]=[]
        ind=[]
        for i in range(len(s)):
            if s[i].isalpha():
                # print("here")
                continue
            # print(i,sdict[lp],sdict[rp])
            # print()
            if s[i]==lp:
                sdict[lp].append(i)
            else:
                if len(sdict[lp])==0:
                    sdict[rp].append(i)
                else:
                    sdict[lp].pop(-1)
        # print(sdict[lp],sdict[rp])
        ind.extend(sdict[lp])
        ind.extend(sdict[rp])
        ind.sort()
        # print(ind)
        ans=""
        st=0
        for i in ind:
            ans=ans+s[st:i]
            st=i+1
        ans=ans+s[st:]
        return ans        
