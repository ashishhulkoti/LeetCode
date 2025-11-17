from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        que = deque()
        deadendSet = set(deadends)
        seen = set()
        seen.add("0000")
        que.append(["0000", 0])
        while que:
            comb, count = que.popleft()
            if comb in deadendSet:
                continue
            if comb == target:
                return count
            
            for i in range(4):
                newCombB = comb[:i] + str(abs(int(comb[i]) + 9)%10) + comb[i+1:]
                newCombF = comb[:i] + str((int(comb[i]) + 1)%10) + comb[i+1:]

                if newCombB not in seen:
                    seen.add(newCombB)
                    que.append([newCombB, count+1])
                if newCombF not in seen:
                    que.append([newCombF, count+1])
                    seen.add(newCombF)
        return -1