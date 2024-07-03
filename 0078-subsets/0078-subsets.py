class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_subset=[]
        curr_subset=[]
        def dfs(i):
            if i==len(nums):
                all_subset.append(curr_subset[:])
                return
            dfs(i+1)
            curr_subset.append(nums[i])
            dfs(i+1)

            curr_subset.pop()
        dfs(0)
        return all_subset


        