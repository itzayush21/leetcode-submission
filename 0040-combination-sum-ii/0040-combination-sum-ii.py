class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()

        def dfs(i,curr,total):
            if total== target:
                temp=curr[::]
                res.append(temp)
                return 
            
            if total>target or i==len(candidates):
                return 

            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])
            curr.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,curr,total)

        dfs(0,[],0)
        return res
        