class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_str={}
        start=0
        count=0
        highest=0
        i=0
        while i < len(s):
            if s[i] not in dict_str:
                dict_str[s[i]]=i
                count+=1
                i+=1
            else:
                i=dict_str[s[i]]+1
                if count > highest:
                    highest=count
                count=0                
                dict_str.clear()
        if count > highest:
            highest=count
        return highest
                    
                

