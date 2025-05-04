# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None
            lefttail=dfs(node.left)
            righttail=dfs(node.right)

            if node.left:
                lefttail.right=node.right
                node.right=node.left
                node.left=None

            last=righttail or lefttail or node
            return last
        return dfs(root)