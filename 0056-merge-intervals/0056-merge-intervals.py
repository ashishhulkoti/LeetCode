class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans=[]
        count=0
        ans.append(intervals[0])
        for interval in intervals:
            left,right=interval
            if left<= ans[count][1]:
                ans[count][1]=max(ans[count][1],right)
            else:
                count+=1
                ans.append(interval)
        return ans
        
