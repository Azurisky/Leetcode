# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < L:
            root = root.right
            if not root:
                return None    
        elif root.val > R:
            root = root.left
            if not root:
                return None
        elif root.val == L:
            root.left = None
        elif root.val == R:
            root.right = None
        
        if root.val > R or root.val < L:
            root = self.trimBST(root, L, R)
        if not root:
            return None
        
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        
        return root