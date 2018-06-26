# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findValue(root):
            val1 = val2 = 0
            if not root:
                return [0, 0]
            l = findValue(root.left) 
            r = findValue(root.right)
            val1 = max(l) + max(r)
            val2 = root.val + l[0] + r[0]
            
            return [val1, val2]
            
        return max(findValue(root))