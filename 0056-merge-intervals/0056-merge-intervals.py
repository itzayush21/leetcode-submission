class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)==1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        m=[]
        for nums in intervals:
            if not m or m[-1][1]<nums[0]:
                m.append(nums)
            else:
                m[-1][1]=max(m[-1][1],nums[1])
        return m
    