class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        while nums1 and nums2:
            if nums1[0]<=nums2[0]:
                arr.append(nums1[0])
                nums1 = nums1[1:]
            elif nums2[0]<nums1[0]:
                arr.append(nums2[0])
                nums2 = nums2[1:]
        while nums1:
            arr.append(nums1[0])
            nums1 = nums1[1:]
        while nums2:
            arr.append(nums2[0])
            nums2 = nums2[1:]
        s, e = 0, len(arr)-1
        if (s+e)%2 == 0:
            return arr[(s+e)//2]
        else:
            return ((arr[(s+e-1)//2]+arr[(s+e+1)//2])/2)
