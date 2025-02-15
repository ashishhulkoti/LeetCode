class MedianFinder:

    def __init__(self):
        self.nums=[]
        self.size=0

    def addNum(self, num: int) -> None:
        l,r=0,self.size-1
        while l<=r:
            mid=l+(r-l)//2
            if num>self.nums[mid]:
                l=mid+1
            else:
                r=mid-1
        self.nums.insert(l,num)
        self.size+=1

    def findMedian(self) -> float:
        if self.size%2==1:
            return self.nums[self.size//2]
        return (self.nums[self.size//2] + self.nums[self.size//2-1])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()