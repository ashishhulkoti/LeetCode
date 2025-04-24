class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        # stack.append(int(s[0]))
        i=0
        # ans=""
        tmpAns=""
        while i < len(s):
            if s[i] == "[" or s[i] >= "a" and s[i] <= "z":
                stack.append(s[i])
            elif s[i] == "]":
                while stack[len(stack)-1] != "[":
                    tmpAns = stack.pop() + tmpAns
                stack.pop()
                num=stack.pop()
                stack.append(tmpAns * num)
                tmpAns=""
            else:
                if len(stack)>0:
                    if isinstance(stack[-1],int):
                        stack.append(stack.pop()*10+int(s[i]))
                    else:
                        stack.append(int(s[i]))
                else:
                    stack.append(int(s[i]))
            i+=1
        return "".join(stack)