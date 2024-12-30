# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return head
        l=0
        temp=head
        while temp is not None:
            temp=temp.next
            l+=1
        temp1=head
        i=0
        while i<l//2-1:
            temp1=temp1.next
            i+=1
        head=temp1.next
        return head
        