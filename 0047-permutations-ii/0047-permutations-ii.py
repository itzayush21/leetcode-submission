class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        perm=[]
        count={n:0 for n in nums}

        for n in nums:
            count[n]+=1

        def dfs():
            if len(perm)==len(nums):
                temp=perm[:]
                res.append(temp)
                return
            
            for n in count:
                if count[n]>0:
                    perm.append(n)
                    count[n]-=1
                
                    dfs()

                    count[n]+=1
                    perm.pop()

        dfs()
        return res
        