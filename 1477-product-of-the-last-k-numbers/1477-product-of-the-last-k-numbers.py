class ProductOfNumbers:

    def __init__(self):
        self.prod_dict={-1:1}
        self.last=-1
        self.zeroes=-1
    def add(self, num: int) -> None:
        self.last+=1        
        if num==0:
            self.prod_dict[self.last]=1
            self.zeroes=self.last
        else:
            self.prod_dict[self.last]=self.prod_dict[self.last-1]*num

    def getProduct(self, k: int) -> int:
        # print(self.prod_dict)
        if (self.last-k+1)>self.zeroes:
            return self.prod_dict[self.last]//self.prod_dict[self.last-k]
        return 0
            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)