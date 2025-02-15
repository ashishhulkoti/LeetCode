class ProductOfNumbers:

    def __init__(self):
        self.prod_list=[]
        self.last=1
    def add(self, num: int) -> None:    
        if num==0:
            self.prod_list.clear()
            self.last=1
        else:
            self.last=self.last*num
            self.prod_list.append(self.last)

    def getProduct(self, k: int) -> int:
        # print(self.prod_dict)
        size=len(self.prod_list)
        if k>size:
            return 0
        elif k==size:
            return self.last
        return self.last//self.prod_list[size-k-1]

            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)