class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_dict={}
        for x in banned:
            banned_dict[x]=1
        count=0
        sumn=0
        for i in range (1,n+1):
            if i in banned_dict:
                continue
            sumn+=i
            if sumn>maxSum:
                return count
            count+=1
            # print(count,sumn)
        return count