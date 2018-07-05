# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ## Build Linked list reversely
        x1, x2 = 0, 0
        while l1:
            x1 = x1*10+l1.val
            l1 = l1.next
        while l2:
            x2 = x2*10+l2.val
            l2 = l2.next
        x = x1 + x2
        
        dummyhead = ListNode(0)
        if x == 0: return dummyhead 
        while x:
            v, x = x%10, x//10
            dummyhead.next, dummyhead.next.next = ListNode(v), dummyhead.next
            if dummyhead.next.next:
                print(dummyhead.next.next.val)
            
        return dummyhead.next
        
        ## 68%
        v1 , v2 = 0, 0
        while l1:
            v1 = v1*10 + l1.val
            l1 = l1.next
        while l2:
            v2 = v2*10 + l2.val
            l2 = l2.next
        
        ans = v1 + v2
        new = head = ListNode(0)
        if not ans:
            return new
        tmp = ans
        count = 0
        while tmp:
            tmp = tmp //10
            count += 1
        count -= 1
        l = len(str(ans))
        while l:
            new.next = ListNode(ans//(10**count))
            ans = ans%(10**count)
            count -= 1
            l -= 1
            new = new.next
        
        return head.next