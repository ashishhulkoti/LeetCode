class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # times=[[0,0]]
        # for i in range(len(startTime)):
        #     times.append([startTime[i],endTime[i]])
        # times.append([eventTime,eventTime])
        # times.sort(key = lambda x : x[0])
        # diff=[]
        # for i in range(len(times)-1):
        #     diff.append(times[i+1][0]-times[i][1])
        startTime.insert(0,0)
        startTime.append(eventTime)
        endTime.insert(0,0)
        endTime.append(eventTime)
        l,h=0,k
        maxSum=0
        currSum=0
        # print(diff)
        diff=[]
        for i in range(len(startTime)-1):
            diff.append(startTime[i+1] - endTime[i])
            if i>h:
                currSum = currSum - (diff[l])
                l+=1
            currSum += diff[i]
            if currSum > maxSum:
                maxSum=currSum
        return maxSum



