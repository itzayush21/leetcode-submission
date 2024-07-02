class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==1:
            return 
        hash={}
        a=[]
        for num in nums:
            if num in hash:
                a.append(num)
            else:
                hash[num]=1
        
        return a

        