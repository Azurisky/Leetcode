# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        tmp = dummy = ListNode(0)
        dummy.next = head
        move = head
        while move and move.next:
            if move.val < move.next.val:
                move = move.next
                continue
            # if tmp.next.val > move.next.val:
            #     tmp = dummy
            
            tmp = dummy
            while move.next.val > tmp.next.val:
                tmp = tmp.next
            nxt = move.next
            move.next = nxt.next
            nxt.next = tmp.next
            tmp.next = nxt    
        
        return dummy.next
            
            
        
        
        