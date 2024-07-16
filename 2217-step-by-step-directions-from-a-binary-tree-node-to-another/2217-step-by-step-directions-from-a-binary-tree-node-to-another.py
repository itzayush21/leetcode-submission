# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def dfs(node,path,target):
            if not node:
                return ""
            if node.val == target:
                return path
            path.append('L')
            res=dfs(node.left,path,target)
            if res:
                return res
            path.pop()
            path.append("R")
            res=dfs(node.right,path,target)
            if res:
                return res


            path.pop()
            return "" 
        
        i=0
        sdist=dfs(root,[],startValue)
        ddist=dfs(root,[],destValue)
        while i< min(len(sdist),len(ddist)):
            if sdist[i]!=ddist[i]:
                break
            i+=1
        
        result=["U"] * len(sdist[i:])+ list(ddist[i:])
        return "".join(result)
        