class Solution:
    def convert(self, s: str, numRows: int) -> str:
        k=0
        rows=[[] for i in range(numRows)]
        
        def ans_helper():
            ans=""
            for x in rows:
                ans+="".join(x)
            return ans
        while True:
            for i in range(0,numRows):
                rows[i].append(s[k])
                k+=1
                if k==len(s):
                    return ans_helper()
            # print(rows)
            for j in range(numRows-2,0,-1):
                rows[j].append(s[k])
                k+=1
                if k==len(s):
                    return ans_helper()
            # print(rows)
            
                
            