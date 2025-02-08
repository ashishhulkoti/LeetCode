# from Collections import SortedSet
class NumberContainers:

    def __init__(self):
        self.indexes={}
        self.number_pos=collections.defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            prev_num=self.indexes[index]
            self.number_pos[prev_num].remove(index)
            if not self.number_pos[prev_num]:
                del self.number_pos[prev_num]
        self.indexes[index]=number
        self.number_pos[number].add(index)


    def find(self, number: int) -> int:
        if number not in self.number_pos:
            return -1
        return self.number_pos[number][0]




# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)