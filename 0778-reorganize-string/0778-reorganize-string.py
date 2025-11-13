import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)
        maxFreq = 0
        for c in s:
            freq[c] += 1
            maxFreq = max(maxFreq, freq[c])
        if maxFreq > (len(s)+1)//2:
            return ""
        ans = [""] * len(s)
        i = 0
        for char, cfreq in sorted(freq.items(), key = lambda x: x[1], reverse = True):
            curFreq = cfreq
            while curFreq > 0 and i<len(s):
                ans[i] = char
                curFreq -= 1
                i += 2
                if i >= len(s):
                    i = 1
        return "".join(ans)





