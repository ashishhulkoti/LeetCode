class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum_diff=float("inf")
        min_array=[]
        for i in range(1,len(arr)):
            diff=abs(arr[i]-arr[i-1])            
            if diff<minimum_diff:
                minimum_diff=diff
                min_array=[]
                min_array.append([arr[i-1],arr[i]])
            elif diff==minimum_diff:
                min_array.append([arr[i-1],arr[i]])
        return min_array
