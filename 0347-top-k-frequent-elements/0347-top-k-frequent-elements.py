class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count=Counter(nums)
        ans=[]
        for num,count in num_count.most_common(k):
            # print(num,count)
            # if count>=k:
            ans.append(num)
        return ans
