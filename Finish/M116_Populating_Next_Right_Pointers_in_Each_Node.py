# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        next = None
        flag = 1
        node = root
        while node:
            if not node.left:
                break
            node.left.next = node.right
            if flag:
                flag = 0
                next = node.left
            if node.next:
                node.right.next = node.next.left
            node = node.next
            if not node and next:
                flag = 1
                node = next
        
        
            
                
        
            
        
        