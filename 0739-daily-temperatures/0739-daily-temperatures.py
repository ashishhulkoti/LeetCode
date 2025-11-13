from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()

        ans = [0] * len(temperatures)

        for i, currTemp in enumerate(temperatures):
            if not stack or temperatures[stack[-1]] >= currTemp:
                stack.append(i)
            while stack and temperatures[stack[-1]] < currTemp:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans
            
