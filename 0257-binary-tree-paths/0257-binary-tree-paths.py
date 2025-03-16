# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        def helper(r):
            if not r:
                return None

            path.append(str(r.val))

            if r.left==None and r.right==None:
                all_path.append("->".join(path))
            
            else:
                helper(r.left)
                helper(r.right)

            path.pop()
        
        path,all_path=[],[]
        helper(root)
        return all_path


        