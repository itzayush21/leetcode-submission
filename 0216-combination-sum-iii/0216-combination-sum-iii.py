class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        l=list(range(1,10))
        res=[]

        def dfs(i,curr,total):
            if total==n and len(curr)==k:
                temp=curr[::]
                res.append(temp)
                return

            if total>n or len(curr)>k or i==len(l):
                return

            curr.append(l[i])
            dfs(i+1,curr,total+l[i])
            curr.pop()

            dfs(i+1,curr,total)

        dfs(0,[],0)
        return res
        