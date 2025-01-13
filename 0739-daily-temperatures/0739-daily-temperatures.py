class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        res=[0]*(len(temperatures))
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                stackt,stackidx=stack.pop()
                res[stackidx]=i-stackidx
            stack.append([t,i])
        return res

        