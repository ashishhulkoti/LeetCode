class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count=0
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i]!=strs[-1][i]:
                return strs[0][:count]
            count+=1
        return strs[0][:count]