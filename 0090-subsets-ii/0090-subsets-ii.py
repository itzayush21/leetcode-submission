class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()

        def dfs(i,subset):
            if i == len(nums):
                temp=subset[::]
                res.append(temp)
                return

            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,subset)


        dfs(0,[])
        return res
        