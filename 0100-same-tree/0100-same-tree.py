# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def helper(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            
            if s.val==t.val:
                return (helper(s.left,t.left) and helper(s.right,t.right)) 
            else:
                return False
            
        return helper(p,q)