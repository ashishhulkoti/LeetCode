class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        sum=0
        numdict={}
        for i in range(len(nums)):
            sum+=nums[i]
            if nums[i] not in numdict:
                numdict[nums[i]]=1
            else:
                numdict[nums[i]]+=1
            
        print(sum)
        largest=float("-inf")
        for i in range(len(nums)):
            sum_complement=(sum-nums[i])/2
            if sum_complement in numdict:
                if (not (numdict[sum_complement]==1 and sum_complement==nums[i])) and nums[i]>largest:
                #     continue
                # if nums[i]>largest:
                    largest = nums[i]
        return largest