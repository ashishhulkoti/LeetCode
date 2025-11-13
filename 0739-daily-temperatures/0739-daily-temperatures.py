from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()

        ans = [0] * len(temperatures)

        for i, currTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < currTemp:
                prevTemp = stack.pop()
                ans[prevTemp] = i - prevTemp
            stack.append(i)
        return ans
            
