# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## Faster 
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None

        ## Map
        if not head:
            return None
        visited = {}
        
        while head.next:
            if head.next in visited:
                return head.next
            else:
                visited[head]=1
                head=head.next
        return None


        ## Math
        if not head:
            return 
        
        quick = slow = head
        
        while True:
            try:
                quick = quick.next.next
            except:
                return
            slow = slow.next
            if quick == slow:
                break
        while head != slow:
            head = head.next
            slow = slow.next
            
        return slow
            