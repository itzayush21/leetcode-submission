# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [0,0]
            l=dfs(root.left)
            r=dfs(root.right)
            no_root=max(l)+max(r)
            with_root=root.val+l[1]+r[1]
            return[with_root,no_root]
        return max(dfs(root))
            
        