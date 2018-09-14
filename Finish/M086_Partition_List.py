# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        ans = new = ListNode(0)
        stack = []
        
        while head:
            if head.val < x:
                new.next = head
                head = head.next
                new.next.next = None
                new = new.next
            else:
                stack.append(head)
                head = head.next
        
        while stack:
            node = stack.pop(0)
            new.next = node
            new.next.next = None
            new = new.next
        
        return ans.next