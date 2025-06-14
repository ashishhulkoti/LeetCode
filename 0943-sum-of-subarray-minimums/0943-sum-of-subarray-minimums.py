class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        arr.append(0)
        minSum = 0
        for i, num in enumerate(arr):
            while stack and num <= arr[stack[-1]]:
                idx = stack.pop()
                prevIdx = -1
                if stack:
                    prevIdx = stack[-1]
                
                minSum += ((i - idx - 1) + (idx - prevIdx - 1) + (i - idx - 1) * (idx - prevIdx - 1) + 1) * arr[idx]
            stack.append(i)
        return minSum % (10**9 + 7)