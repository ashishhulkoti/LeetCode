from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1_count = Counter(s)
        chars_in_s = len(s)
        for c in t:
            if c in s1_count:
                s1_count[c] -= 1
                chars_in_s -= 1
                if s1_count[c] == 0:
                    del s1_count[c]
        return chars_in_s
            