class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        max_h = len(citations)
        for paperNo, paper in enumerate(citations):
            if paper >= max_h - paperNo:
                return max_h - paperNo
        return 0
