class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        left_mht,right_mht=0,0
        l,r=0,len(height)-1
        water=0
        while l<r:
            # print(l,r)
            if height[l]<height[r]:
                if height[l]>left_mht:
                    left_mht=height[l]
                water+=left_mht-height[l]
                l+=1
            else:
                if height[r]>right_mht:
                    right_mht=height[r]
                water+=right_mht-height[r]
                r-=1
        return water