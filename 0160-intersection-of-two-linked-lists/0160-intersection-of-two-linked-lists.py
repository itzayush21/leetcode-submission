# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def len_list(head):
            temp=head
            l=-1
            while temp:
                l+=1
                temp=temp.next
            return l
        
        lenA=len_list(headA)
        lenB=len_list(headB)

        while lenA>lenB:
            lenA-=1
            headA=headA.next
        
        while lenA<lenB:
            lenB-=1
            headB=headB.next
        
        while headA != headB:
            print(headA.val,headB.val)
            headA=headA.next
            headB=headB.next
        
        return headA
        