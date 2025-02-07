class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        b_dict={}
        c_dict={}
        count=0
        ans=[]
        for b,c in queries:
            
            if b not in b_dict:
                b_dict[b]=c
                if c in c_dict:
                    c_dict[c]+=1
                else:
                    c_dict[c]=1
                    count+=1
            else:
                oc=b_dict[b]
                if c_dict[oc]==1:
                    del c_dict[oc]
                    count-=1
                else:
                    c_dict[oc]-=1
                b_dict[b]=c
                if c in c_dict:
                    c_dict[c]+=1
                else:
                    c_dict[c]=1
                    count+=1
            ans.append(count)
        return ans