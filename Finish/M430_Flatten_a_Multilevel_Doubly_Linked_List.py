"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        ans = new = Node(0, None, None, None)
        stack = [head]
        while stack:
            node = stack.pop()
            
            ans.next = node
            node.prev = ans
            ans.child = None
            
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
            
            ans = node
        new.next.prev = None
        return new.next