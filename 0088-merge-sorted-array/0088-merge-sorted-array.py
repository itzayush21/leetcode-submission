class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a=m-1
        b=n-1
        ind=m+n-1

        while b>=0:
            if a>=0 and nums1[a]>nums2[b]:
                nums1[ind]=nums1[a]
                ind-=1
                a-=1

            else:

                nums1[ind]=nums2[b]
                ind-=1
                b-=1

        return nums1
                