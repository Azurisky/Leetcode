# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        new = ListNode(head.val)
    
        while head.next:
            tmp = ListNode(head.next.val)
            tmp.next = new
            new = tmp
            head = head.next
        return tmp
        
        ## Faster
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur:
            p = cur.next
            cur.next = prev
            prev = cur
            cur = p
        return prev