import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        heapq.heapify(nums)
        ops=0
        while len(nums)>=2:
            num1=heapq.heappop(nums)
            if num1<k:
                num2=heapq.heappop(nums)
                heapq.heappush(nums,num2+num1*2)
                ops+=1
            else:
                break
        return ops