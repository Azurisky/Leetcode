class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

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