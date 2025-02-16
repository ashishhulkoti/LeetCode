import math
class RandomizedSet:

    def __init__(self):
        self.present_check={}
        self.index_num={}
        self.count=0

    def insert(self, val: int) -> bool:
        if val in self.present_check:
            return False
        else:
            self.present_check[val]=self.count
            self.index_num[self.count]=val
            self.count+=1
            return True

    def remove(self, val: int) -> bool:
        if val in self.present_check:
            if self.count==1:
                self.index_num={}
                self.present_check={}
                self.count-=1
                return True
            to_be_deleted_ind=self.present_check[val]
            new_val=self.index_num[self.count-1]
            self.present_check[new_val]=to_be_deleted_ind
            self.index_num[to_be_deleted_ind]=new_val
            del self.index_num[self.count-1]
            del self.present_check[val]
            self.count-=1
            return True
        else:
            return False

    def getRandom(self) -> int:
        x=random.random()
        ind=math.ceil(x*self.count)-1
        return self.index_num[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()