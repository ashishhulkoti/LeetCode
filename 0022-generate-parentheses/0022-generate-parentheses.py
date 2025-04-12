class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def paraHelper(lp,rp,comb):
            nonlocal ans,n
            if lp==n and rp==n:
                ans.append(comb)
                return
            if lp<n:
                paraHelper(lp+1,rp,comb+"(")
            if rp<lp:
                paraHelper(lp,rp+1,comb+")")
            return
        paraHelper(1,0,"(")
        return ans
