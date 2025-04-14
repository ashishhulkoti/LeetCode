class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        highestArea=heights[0]
        stack.append([0,heights[0],0])
        for i in range(1,len(heights)):
            if heights[i] >= stack[-1][1]:
                stack.append([i,heights[i],0])
            else:
                carry=0
                numH=0
                while stack and heights[i] <= stack[-1][1]:
                    idx,ht,carryht=stack.pop()
                    carry+=carryht
                    numH+=1
                    if (i - idx + carryht)*ht > highestArea:
                        highestArea = (i - idx + carryht)*ht
                stack.append([i,heights[i],numH+carry])
        while stack:
            idx,ht,carryht=stack.pop()
            if (len(heights) - idx + carryht)*ht > highestArea:
                highestArea = (len(heights)-idx+carryht)*ht
        
        return highestArea


            