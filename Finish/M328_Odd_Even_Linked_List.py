# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
         

        ## 100% 
        node = head
        odd = head
        head_even = even = ListNode(0)
        if not head:
            return None
        
        while odd:
            if odd.next:
                even.next = odd.next
                even = even.next   
            else:
                break
            if even.next:
                odd.next = even.next
                odd = odd.next
            else:
                break
                
        odd.next = head_even.next
        even.next = None
        return head

        ## old
        if not head or not head.next:
            return head

        odd = head
        even = get = head.next
        
        while odd and odd.next and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = get
        return head
        