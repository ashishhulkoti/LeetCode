class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels={"a":1,"i":1,"e":1,"o":1,"u":1}
        ranges={}
        ranges[-1]=0
        count=0
        for index,word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count+=1
            ranges[index]=count
        ans=[]
        for l,r in queries:
            ans.append(ranges[r]-ranges[l-1])
        return ans