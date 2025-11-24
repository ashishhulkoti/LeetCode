class Solution:
    def __init__(self):
        self.index = 0

    def decodeString(self, s: str) -> str:
        result = []
        
        while self.index < len(s) and s[self.index] != ']':
            if not s[self.index].isdigit():  
                result.append(s[self.index])
                self.index += 1
            else:
                # build the number k
                k = 0
                while self.index < len(s) and s[self.index].isdigit():
                    k = k * 10 + int(s[self.index])
                    self.index += 1

                self.index += 1  # skip '['

                decoded = self.decodeString(s)

                self.index += 1  # skip ']'

                result.append(decoded * k)
        
        return "".join(result)
