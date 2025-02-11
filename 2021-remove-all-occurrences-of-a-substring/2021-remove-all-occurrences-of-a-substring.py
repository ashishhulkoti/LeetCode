class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        tmp_stack=[]
        p_last_ind=len(part)-1
        for x in s:
            stack.append(x)
            if x==part[p_last_ind]:
                while p_last_ind>=0 and stack:
                    char=stack.pop()
                    tmp_stack.insert(0,char)
                    if char!=part[p_last_ind]:
                        break
                    p_last_ind-=1
                if p_last_ind!=-1:
                    stack.extend(tmp_stack)
                tmp_stack=[]
                p_last_ind=len(part)-1
        return "".join(stack)                

