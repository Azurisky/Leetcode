# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first, second = head, head.next
        while second and second.next:
            first, second = first.next, second.next.next
        tmp = first.next
        first.next = None
        l = self.sortList(head)
        r = self.sortList(tmp)
        return self.merge(l, r)
        
    def merge(self, l, r):
        if not l or not r:
            return l or r

        if l.val > r.val:
            r, l = l, r

        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp

            pre = pre.next
        pre.next = l or r
        return head
                
                
            
                