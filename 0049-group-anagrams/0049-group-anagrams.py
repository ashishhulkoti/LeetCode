class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict={}
        if len(strs)==1:
            return [[strs[0]]]
        for x in strs:
            sorted_str=''.join(sorted(x))
            if sorted_str in str_dict:
                str_dict[sorted_str].append(x)
            else:
                str_dict[sorted_str]=[x]
        ans=[]
        for key,value in str_dict.items():
            ans.append(value)
        return ans