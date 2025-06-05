class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack=[]
        for i,n in enumerate(nums):

            while stack and stack[-1]>n and len(stack)+(len(nums)-i)>k:
                stack.pop()
            
            if len(stack)<k:
                stack.append(n)

        return stack
        