class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=[]
        k=0
        for i in nums1:
            l.append(i)
        for i in nums2:
            l.append(i)
        l.sort()
        if len(l)%2==0:
            k=float(l[(len(l)//2)-1]+l[len(l)//2])/2
            
        else:

            k=l[len(l)//2]

        return k

        