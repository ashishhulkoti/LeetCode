class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack=[]
        tstack=[]

        for x in s:
            if x=="#":
                if sstack:
                    sstack.pop()
            else:
                sstack.append(x)

        for x in t:
            if x=="#":
                if tstack:
                    tstack.pop()
            else:
                tstack.append(x)
        return sstack==tstack
        