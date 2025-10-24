class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        old_stack = []
        new_stack = []
        binary_changed = False
        count = 0
        iterator = 0

        while iterator < len(s):
            if new_stack and s[iterator] == s[new_stack[-1]]:
                new_stack.append(iterator)
            else:
                if old_stack:
                    count += min(len(old_stack),len(new_stack))
                old_stack = new_stack
                new_stack = [iterator]
            iterator += 1
        return count + min(len(old_stack),len(new_stack))
        

            
                


            

