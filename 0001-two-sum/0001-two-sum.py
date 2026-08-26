class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ele={}
        res=[]

        for i,n in enumerate(nums):
            if target-nums[i] in ele:
                return [ele[target-nums[i]],i]

            ele[nums[i]]=i

        return res
        
        