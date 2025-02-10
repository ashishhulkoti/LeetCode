class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for x in s:
            if x.isalpha():
                stack.append(x)
            elif len(stack)>0:
                stack.pop()
        return "".join(stack)