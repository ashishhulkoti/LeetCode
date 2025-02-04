class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            if i<=j:
                word+=word1[i]
                i+=1
            else:
                word+=word2[j]
                j+=1
        # print(word1[i:len(word1)])
        if i==len(word1):
            word=word+word2[j:len(word2)]
        else:
            word=word+word1[i:len(word1)]
        return word
            