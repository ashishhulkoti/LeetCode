class Bitset:

    def __init__(self, size: int):
        self.bitarray = [0] * size
        self.size = size
        self.sum = 0
        self.flipFlag = False

    def fix(self, idx: int) -> None:
        if self.flipFlag and self.bitarray[idx] == 1:
            self.bitarray[idx] = 0
            self.sum -= 1
        elif not self.flipFlag and self.bitarray[idx] == 0:
            self.bitarray[idx] = 1
            self.sum += 1

    def unfix(self, idx: int) -> None:
        if self.flipFlag and self.bitarray[idx] == 0:
            self.bitarray[idx] = 1
            self.sum += 1
        elif not self.flipFlag and self.bitarray[idx] == 1:
            self.bitarray[idx] = 0
            self.sum -= 1

    def flip(self) -> None:
        self.flipFlag = not self.flipFlag

    def all(self) -> bool:
        return True if (not self.flipFlag and self.sum == self.size) or (self.flipFlag and self.sum == 0) else False

    def one(self) -> bool:
        return True if (not self.flipFlag and self.sum >=1) or (self.flipFlag and self.sum < self.size) else False

    def count(self) -> int:
        return self.size - self.sum if self.flipFlag else self.sum

    def toString(self) -> str:
        if not self.flipFlag:
            return "".join(map(str, self.bitarray))
        ans=""
        for x in self.bitarray:
            ans = ans + str(1-x)
        return ans


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()