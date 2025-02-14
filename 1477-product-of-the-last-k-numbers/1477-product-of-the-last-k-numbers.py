class ProductOfNumbers:

    def __init__(self):
        self.prod_dict={-1:1}
        self.last=-1
        self.zeroes=SortedList([])
    def add(self, num: int) -> None:
        if num==0:
            self.prod_dict[self.last+1]=1
            self.zeroes.add(self.last+1)
        else:
            self.prod_dict[self.last+1]=self.prod_dict[self.last]*num
        self.last+=1

    def getProduct(self, k: int) -> int:
        if len(self.zeroes)==0 or (self.last-k+1)>self.zeroes[-1]:
            return self.prod_dict[self.last]//self.prod_dict[self.last-k]
        return 0
            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)