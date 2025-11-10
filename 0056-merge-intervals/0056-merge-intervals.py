class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0], x[1]))
        mergedIntervals = [intervals[0]]

        i = 1
        while i < len(intervals):
            if intervals[i][0] <= mergedIntervals[-1][1]:
                mergedIntervals[-1][1] = max(intervals[i][1], mergedIntervals[-1][1])
            else:
                mergedIntervals.append(intervals[i])
            i+=1
        return mergedIntervals