# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        
        first = head
        ans = second = ListNode(0)
        second.next = head
        
        for i in range(n):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        
        return ans.next
        
            
        
            