class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(heights)
        stack.append(0)    

        for i in range(1,len(heights)):
            if heights[i] >= heights[stack[-1]]:
                while stack:
                    if heights[stack[-1]] > heights[i]:
                        answer[stack[-1]] += 1
                        break
                    idx = stack.pop()
                    answer[idx] += 1
            else:
                    answer[stack[-1]] += 1
            
            stack.append(i)
        return answer