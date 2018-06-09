# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans = head = ListNode(0)
        n = 0
        while n < len(lists):
            n = 0
            mi = float('inf')
            for i in lists:
                if i:
                    if mi > i.val:
                        mi = i.val
            
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val == mi:
                        ans.next = ListNode(mi)
                        ans = ans.next
                        lists[i] = lists[i].next
            
            for i in lists:
                if not i:
                    n += 1
        return head.next

## Better version, Use heap queue
        import heapq
               
        outll = temp = ListNode(0)
        k = len(lists)    
        if k == 0:
            return None
        
        bigheap = []
        counter = 0
        for i in lists:
            while i:
                heapq.heappush(bigheap, (i.val, counter, i))
                i = i.next
                counter += 1
        
        if len(bigheap) == 0:
            return None
        
        while bigheap:
            temp.next = heapq.heappop(bigheap)[2]
            temp = temp.next
            
        return outll.next

## Best version, only store the value 
        outll = temp = ListNode(0)
        k = len(lists)    
        if k == 0:
            return None
        
        biglist = list()
        for i in lists:
            while i:
                biglist.append(i.val)
                i = i.next
        
        if len(biglist) == 0:
            return None
        
        for i in sorted(biglist):
            nnode = ListNode(i)
            temp.next = nnode
            temp = temp.next
            
        return outll.next