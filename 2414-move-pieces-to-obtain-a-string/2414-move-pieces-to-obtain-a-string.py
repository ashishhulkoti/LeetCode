class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sl,tl=0,0

        while True: 
            while tl<len(target):
                if target[tl]!="_":
                    break
                tl+=1
            if tl==len(target):
                for i in range(sl,len(start)):
                    if start[i]=="L" or start[i]=="R":
                        return False
                return True
            while sl < len(start):
                if start[sl]!="_":
                    break
                sl+=1
            if sl ==len(start):
                return False
            
            if start[sl]!=target[tl] or (target[tl]=="R" and sl > tl) or (target[tl]=="L" and sl < tl):
                return False
            tl+=1
            sl+=1
        return True
            