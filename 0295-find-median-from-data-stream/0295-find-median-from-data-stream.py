class MedianFinder:

    def __init__(self):
        self.nums=[]

    def addNum(self, num: int) -> None:
        if len(self.nums)==0:
            self.nums.append(num)
        else:
            l,r=0,len(self.nums)-1
            while l<=r:
                mid=l+(r-l)//2
                if self.nums[mid]==num:
                    self.nums.insert(mid,num)
                    return
                elif num>self.nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            if l==len(self.nums):
                self.nums.append(num)
            else:
                self.nums.insert(l,num)

    def findMedian(self) -> float:
        # print(self.nums)
        if len(self.nums)%2==1:
            return self.nums[len(self.nums)//2]
        return (self.nums[len(self.nums)//2] + self.nums[len(self.nums)//2-1])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()