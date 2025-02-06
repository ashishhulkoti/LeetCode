class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
        elif n==0:
            pass
        else:
            k=m+n-1
            i,j=m-1,n-1
            while i>=0 and j>=0:
                if nums1[i] > nums2[j]:
                    nums1[k]=nums1[i]
                    i-=1
                else:
                    nums1[k]=nums2[j]
                    j-=1
                k-=1
            if i==-1:
                for x in range(j,-1,-1):
                    nums1[x]=nums2[x]        