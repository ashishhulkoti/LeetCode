class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # seqs=[]
        # candidates.sort()
        nums=Counter(candidates)
        # print(nums)
        dp=[]
        for i in range(target+1):
            dp.append([])
        # print(dp)
        # return []
        
        for s in range(1,target+1):
            if s in nums:
                dp[s].append([s])
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

        
