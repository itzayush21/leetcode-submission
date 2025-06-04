class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        res=-1
        for _ in range(len(nums)-k+1):
            res=heapq.heappop(nums)

        return res
        