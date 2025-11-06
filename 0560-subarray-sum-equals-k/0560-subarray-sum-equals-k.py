from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currSum = 0
        cache = defaultdict(int)
        cache[0] = 1
        for x in nums:
            currSum += x
            if currSum - k in cache:
                count+=cache[currSum - k]
            cache[currSum] += 1
            # cumulativeSum.append(currSum)
            # if currSum == k:
            #     count += 1

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if cumulativeSum[j] - cumulativeSum[i] == k:
        #             count += 1
        return count