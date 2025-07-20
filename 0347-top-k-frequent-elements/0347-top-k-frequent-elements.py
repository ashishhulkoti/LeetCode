from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        hp = []
        heapq.heapify(hp)
        for key, value in counts.items():
            heapq.heappush(hp,(-1 * value,key))
        ans=[]
        for _ in range(k):
            ans.append(heapq.heappop(hp)[1])
        return ans