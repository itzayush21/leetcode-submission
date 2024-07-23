class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        def custom_sort(n):
            return (d[n],-n)
        nums.sort(key=custom_sort)
        return nums

        