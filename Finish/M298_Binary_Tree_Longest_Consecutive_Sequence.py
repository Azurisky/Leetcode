# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if not root:
            return 0
        stack = [[root, 1]]
        while stack:
            node, l = stack.pop()
            if node.left:
                if node.val == node.left.val-1:
                    stack.append([node.left, l+1])
                else:
                    stack.append([node.left, 1])
            if node.right:
                if node.val == node.right.val-1:
                    stack.append([node.right, l+1])
                else:
                    stack.append([node.right, 1])
            ans = max(ans, l)
        return ans
            
        
        