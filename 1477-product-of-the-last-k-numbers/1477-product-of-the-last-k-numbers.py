class ProductOfNumbers:

    def __init__(self):
        self.prod_list=[]
        self.last=1
        self.size=0
    def add(self, num: int) -> None:    
        if num==0:
            self.prod_list=[]
            self.last=1
            self.size=0
        else:
            self.last=self.last*num
            self.prod_list.append(self.last)
            self.size+=1

    def getProduct(self, k: int) -> int:
        if k>self.size:
            return 0
        elif k==self.size:
            return self.last
        return self.last//self.prod_list[self.size-k-1]

            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)