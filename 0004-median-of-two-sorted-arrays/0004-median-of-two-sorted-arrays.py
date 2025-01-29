class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1,p2=0,0
        count=1
        m,n=len(nums1),len(nums2)
        even=False
        first,second=0,0
        while p1<= m-1 and p2<=n-1 and count<=(m+n)//2+1:
            if nums1[p1]<nums2[p2]:
                # nums.append(nums1[p1])
                first=second
                second=nums1[p1]
                p1+=1
            else:
                # nums.append(nums2[p2])
                first=second
                second=nums2[p2]
                p2+=1
            count+=1
        print(p1,p2,count)
        if count!=(m+n)//2+2:
            if p1==m:
                while count<=(m+n)//2+1:
                    first=second
                    second=nums2[p2]
                    p2+=1
                    count+=1
            else:
                while count<=(m+n)//2+1:
                    first=second
                    second=nums1[p1]
                    p1+=1
                    count+=1
        if ((m+n)%2 == 0):
            return (second+first)/2
        else:
            return second

