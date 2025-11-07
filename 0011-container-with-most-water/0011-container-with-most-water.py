class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

        l, r = 0, len(height) - 1
        while l<r:
            max_water = max(max_water, abs((r - l)*min(height[r],height[l])))
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
        return max_water
