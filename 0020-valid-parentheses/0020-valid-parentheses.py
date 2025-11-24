class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == '}' or s[i] == ')' or s[i] == ']':
                if not stack:
                    return False 
                top = stack.pop()
                if top == '{' and s[i] is not '}' :
                    return False
                elif top == '(' and s[i] is not ')':
                    return False
                elif top == '[' and s[i] is not ']':
                    return False
        if len(stack) > 0 : 
            return False
        return True
                               
        