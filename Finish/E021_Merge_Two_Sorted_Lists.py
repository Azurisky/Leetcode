# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        ans = head = ListNode(0)
        
        while l1 and l2:
            print(ans.val)
            if l1.val < l2.val:
                ans.next = ListNode(l1.val)
                ans = ans.next
                l1 = l1.next
            else:
                ans.next = ListNode(l2.val)
                ans = ans.next
                l2 = l2.next
        if not l1:
            ans.next = l2
        else:
            ans.next = l1
        
        return head.next