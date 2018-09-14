"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        ## iterative
        if not root:
            return None
            
        stack = []
        curr = root
        head = prev = Node(0, None, None)
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if stack:
                    curr = stack.pop()
                    # print(curr.val)
                    prev.right = curr
                    curr.left = prev
                    prev = curr
                    curr = curr.right
        head = head.right
        prev.right = head
        head.left = prev
        
        return head    


        ## recursive
        def inorder(node):
            if not node.left and not node.right:
                return node, node
            if node.left:
                headLeft, tailLeft = inorder(node.left)
                tailLeft.right = node
                node.left = tailLeft
            else:
                headLeft, tailLeft = node, node
                
            if node.right:
                headRight, tailRight = inorder(node.right)
                headRight.left = node
                node.right = headRight
            else:
                headRight, tailRight = node, node
            return headLeft, tailRight
        
        if not root:
            return None
        head, tail = inorder(root)
        head.left = tail
        tail.right = head
        return head
                