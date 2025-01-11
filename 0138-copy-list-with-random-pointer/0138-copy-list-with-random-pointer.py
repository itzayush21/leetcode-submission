"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        temp=head
        while temp:
            copy_node=Node(temp.val)
            copy_node.next=temp.next
            temp.next=copy_node
            temp=temp.next.next
        
        temp=head
        while temp:
            copy_node=temp.next
            if temp.random:
                copy_node.random=temp.random.next
            else:
                copy_node.random=None
            temp=temp.next.next
        
        temp=head
        dummy=Node(-1)
        res=dummy

        while temp:
            res.next=temp.next
            res=res.next

            temp.next=temp.next.next
            temp=temp.next

        return dummy.next
        