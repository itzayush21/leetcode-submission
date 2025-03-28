"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        old2new={}
        def dfs(node):
            if node in old2new:
                return old2new[node]
            copy=Node(node.val)
            old2new[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        return dfs(node) if node else None
        