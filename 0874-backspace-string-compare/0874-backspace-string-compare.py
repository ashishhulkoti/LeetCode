class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def stringHelper(tmpstr):
            bs=0
            ans=[]
            for i in range(len(tmpstr)-1,-1,-1):
                if tmpstr[i]=="#":
                    bs+=1
                else:
                    if bs==0:
                        ans.insert(0,tmpstr[i])
                    else:
                        bs-=1
            
            return "".join(ans)
        
        if stringHelper(s)==stringHelper(t):
            return True
        return False
