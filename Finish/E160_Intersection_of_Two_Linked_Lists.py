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
        ## Truncate the long one
        if not headA or not headB:
            return None

        lena, t = 0, headA
        while t:
            lena, t = lena + 1, t.next

        lenb, t = 0, headB
        while t:
            lenb, t = lenb + 1, t.next

        if lena > lenb:
            lena, lenb, headA, headB = lenb, lena, headB, headA

        while lenb > lena:
            lenb, headB = lenb - 1, headB.next

        while headA != headB:
            headA, headB = headA.next, headB.next

        return headA


        ## Concat two list
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA

        return pa if pa is not None else None

        ## Revert the list
        def revert(head):
            if head == None:
                return head
            prev = None
            curr = head
            res = ListNode(None)
            while curr:
                res.val = curr.val
                prev = ListNode(None)
                prev.next = res
                res = prev
                curr = curr.next
            return res.next

        root1,root2 = revert(headA), revert(headB)
        result, curr1, curr2 = ListNode(None), root1, root2
        root,prev = result, None
        while curr1 and curr2 and curr1.val == curr2.val:
            result.val, result.next = curr1.val, ListNode(None)
            prev,result = result,result.next
            curr1, curr2 = curr1.next, curr2.next
        if prev:
            prev.next = None
        if root.val:
            return revert(root)
        else:      
            return None