class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size=len(nums1)+len(nums2)
        nums3=[]
        mid=size//2
        count,i,j=0,0,0
        while i+j <= mid and nums1 and nums2:
            if nums1[0]<nums2[0]:
                nums3.append(nums1[0])
                # print("Popping1 : ",nums1[0])
                nums1.pop(0)
                i+=1
            else:
                nums3.append(nums2[0])
                # print("Popping2 : ",nums2[0])
                nums2.pop(0)
                j+=1
        if 0==len(nums1):
            nums3.extend(nums2)
        if 0==len(nums2):
            nums3.extend(nums1)
        # print(nums3,mid)
        if size%2==0:
            return (nums3[mid]+nums3[mid-1])/2
        return nums3[mid]