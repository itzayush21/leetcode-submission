class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d={n:i for i,n in enumerate(nums1)}
        res=[-1]*len(nums1)
        stack=[]
        for j in nums2:
            curr=j
            while stack and curr>stack[-1]:
                val=stack.pop()
                idx=d[val]
                res[idx]=curr
            if curr in nums1:
                stack.append(curr)
        return res




        