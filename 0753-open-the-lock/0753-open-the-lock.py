from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        que = deque()
        deadendSet = set(deadends)
        seen = set()
        que.append(["0000", 0])

        while que:
            comb, count = que.popleft()
            if comb in deadendSet or comb in seen:
                continue
            seen.add(comb)
            if comb == target:
                return count
            
            for i in range(4):
                newCombB, newCombF = list(comb), list(comb)
                newCombB[i] = str(abs(int(comb[i]) + 9)%10)
                newCombF[i] = str((int(comb[i]) + 1)%10)
                newCombB = "".join(newCombB)
                newCombF = "".join(newCombF)
                if newCombB not in seen:
                    que.append([newCombB, count+1])
                if newCombF not in seen:
                    que.append([newCombF, count+1])
        return -1