class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_items=sorted(Counter(nums).most_common(),reverse=True)
        sum=0
        for n,c in sorted_items:
            sum+=c
            if sum>=k:
                return n
