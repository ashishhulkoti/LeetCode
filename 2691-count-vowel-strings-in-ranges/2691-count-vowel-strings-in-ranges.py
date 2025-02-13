class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels={"a":1,"i":1,"e":1,"o":1,"u":1}
        ranges=[]
        count=0
        for word in words:
            ranges.append(count)
            if word[0] in vowels and word[-1] in vowels:
                count+=1
                # print("yes")
        ranges.append(count)
        ans=[]
        for l,r in queries:
            ans.append(ranges[r+1]-ranges[l])
        return ans