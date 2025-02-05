class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # sum=0
        last=len(nums)-1
        ans=[]
        num_dict={}
        # print(nums)
        for i in range(len(nums)-2):
            l,r=i+1,last
            num=0-nums[i]
            while l<r:
                sum=nums[l]+nums[r]
                if num==sum:
                    num_str=str(nums[i])+str(nums[l])+str(nums[r])
                    if num_str not in num_dict:
                        ans.append([nums[i],nums[l],nums[r]])
                        num_dict[num_str]=1
                    l+=1
                    r-=1
                elif sum<num:
                    l+=1
                else:
                    r-=1
            i+=1
        return ans

