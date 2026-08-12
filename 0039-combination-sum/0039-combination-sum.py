class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def dfs(i,curr):
            if sum(curr)>target:
                return
            if sum(curr)==target:
                if curr not in res:
                    res.append(curr[:])

            if i == len(candidates):
                return

            curr.append(candidates[i])
            dfs(i, curr)
            curr.pop()

            dfs(i+1,curr)


        dfs(0,[])

        return res
            
        