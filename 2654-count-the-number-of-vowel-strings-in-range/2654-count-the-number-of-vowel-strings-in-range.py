class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count=0
        vowels={"a":1,"e":1,"i":1,"o":1,"u":1}
        for i in range(left,right+1):
            if (words[i][0] in vowels) and (words[i][-1] in vowels):
                count+=1
        return count