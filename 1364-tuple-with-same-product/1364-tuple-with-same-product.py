class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        num_dict={}
        tuple_dict={}
        if len(nums)<=3:
            return 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod=nums[i]*nums[j]
                if prod in num_dict:
                    num_dict[prod]+=1
                    tuple_dict[prod]=1
                else:
                    num_dict[prod]=1
        count=0
        for x in list(tuple_dict.keys()):
            # print(x,num_dict[x][0],2**num_dict[x][0],num_dict[x][1])
            count+=(num_dict[x]*(num_dict[x]-1))*4
        return count
                    