class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp=[]
        for i in range(target+1):
            dp.append([])
        for x in candidates:
            if x<=target:
                dp[x].append([x])
        for s in range(1,target+1):
            i,j=1,s-1
            while i<=j:
                if len(dp[i])!=0 and len(dp[j])!=0:
                    for k in dp[i]:
                        for l in dp[j]:
                            tmp = k+l
                            tmp.sort()
                            if tmp not in dp[s]:
                                dp[s].append(k+l)
                i+=1
                j-=1
        return dp[-1]

        
