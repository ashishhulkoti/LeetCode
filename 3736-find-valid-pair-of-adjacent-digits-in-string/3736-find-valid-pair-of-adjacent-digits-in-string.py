class Solution:
    def findValidPair(self, s: str) -> str:
        nums_dict=Counter(s)
        flag=False
        # print(nums_dict)
        if nums_dict[s[0]]==int(s[0]):
            flag=True
        for i in range(1,len(s)):
            if nums_dict[s[i]]==int(s[i]):
                if s[i]!=s[i-1] and flag:
                    return s[i-1]+s[i]
                flag=True
            else:
                flag=False
        return ""
