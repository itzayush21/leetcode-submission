# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        vis = set()
        v = {}
        for r, c, isLeft in descriptions:
            if r not in v:
                v[r] = TreeNode(r)
            if c not in v:
                v[c] = TreeNode(c)
            if isLeft:
                v[r].left = v[c]
            else:
                v[r].right = v[c]
            vis.add(c)
        for i, node in v.items():
            if i not in vis:
                return node