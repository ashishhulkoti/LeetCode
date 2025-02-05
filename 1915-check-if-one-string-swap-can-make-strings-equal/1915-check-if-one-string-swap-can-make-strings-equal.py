class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s_dict={}
        ind=[]
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                ind.append(k)
        if len(ind)>2 or len(ind)==1:
            return False
        elif len(ind)==0 or (len(ind)==2 and s1[ind[0]]==s2[ind[1]] and s1[ind[1]]==s2[ind[0]]):
            return True
        return False