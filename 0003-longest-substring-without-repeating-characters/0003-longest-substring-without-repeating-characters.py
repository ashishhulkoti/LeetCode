class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        size=len(s)
        longest=1
        dict_s={}
        if size==0:
            return 0
        if s==1:
            return 1
        while right<size:
            if s[right] not in dict_s:
                dict_s[s[right]]=right
                right+=1
            else:
                if right-left>longest:
                    longest=right-left   
                del dict_s[s[left]]
                left+=1
        if len(dict_s)>longest:
            return len(dict_s)
        return longest

                