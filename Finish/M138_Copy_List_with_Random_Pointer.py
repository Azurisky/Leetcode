# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        start = head
        while head:
            node = RandomListNode(head.label)
            tmp = head.next
            head.next = node
            node.next = tmp 
            head = tmp
        
        second = start
        while second:
            # print(second.label)
            nxt = second.next.next
            if second.random:
                second.next.random = second.random.next
            second = nxt 
            
        third = start
        start = start.next
        while third:
            nxt = third.next.next
            if nxt:
                third.next.next = nxt.next
            third.next = nxt
            third = nxt
        return start
            
        
        
    
        