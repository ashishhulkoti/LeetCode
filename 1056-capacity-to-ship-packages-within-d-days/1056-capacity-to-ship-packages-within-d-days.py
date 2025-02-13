import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def feasible(msum):
            count=0
            tmpsum=0
            for i in range(len(weights)):
                tmpsum+=weights[i]
                if tmpsum>msum:
                    count+=1
                    tmpsum=weights[i]
            return count
        
        total_weight=0
        max_weight=0
        
        for j in range(len(weights)):
            if weights[j]>max_weight:
                max_weight=weights[j]
            total_weight+=weights[j]
        
        

        l=max_weight
        r=total_weight
        # print(l,r)
        while l<=r:
            mid=l+(r-l)//2
            currcount=feasible(mid)
            print(mid,currcount)
            if currcount<days:
                r=mid-1
            else:
                l=mid+1
        # print(l)
        return l