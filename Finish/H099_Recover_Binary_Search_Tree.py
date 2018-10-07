# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        def swap(node1, node2):
            node1.val, node2.val = node2.val, node1.val

        first, second = None, None
        prev = None
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node
                
            prev = node
            root = node.right
        
        swap(first, second)
