class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        ## two pointer    
        if not head or not head.next:
            return 
        
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tmp = slow.next
        slow.next = None
        
        def reverseList(node):
            head = ListNode(0)
            while node:
                prev = head.next
                nxt = node.next
                head.next = node
                node.next = prev
                node = nxt
            return head.next
        
        tail = reverseList(tmp)

        ans = head
        while tail:
            nxt = head.next
            head.next = tail
            tail = tail.next
            head.next.next = nxt
            head = nxt
        if tail:
            head.next = tail
        # return ans
        

        ## 40%
        if head == None or head.next == None:
            return
        
        tmp = head
        stack = []
        while tmp:
            stack.append(tmp)
            tmp = tmp.next
        t1 = head
        t2 = head.next
        leng = len(stack)
        l = leng//2
        while l > 0:
            node = stack.pop()
            t1.next = node
            node.next = t2
            t1 = t2
            t2 = t2.next
            l -= 1
        if leng%2 == 0:
            t2.next = None
        else:
            t2.next = stack.pop()
            t2.next.next = None