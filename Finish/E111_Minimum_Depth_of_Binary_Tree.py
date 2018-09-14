# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        level = 0
        while queue:
            tmp = []
            level += 1
            for node in queue:
                if not node.left and not node.right:
                    return level
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue, tmp = tmp, []
        
                