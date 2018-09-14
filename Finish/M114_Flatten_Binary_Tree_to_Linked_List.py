# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        ## While loop
        while root:
            if root.left:
                tmp = root.right
                cur = root.left
                while cur.right:
                    cur = cur.right
                root.right = root.left
                root.left = None
                cur.right = tmp
            root = root.right
             

        ## Recursive
        if not root:
            return
        self.prev = root
        self.flatten(root.left)
        tmp = root.right
        root.right = root.left
        root.left = None
        
        self.prev.right = tmp
        self.flatten(tmp)
        

        
        
                