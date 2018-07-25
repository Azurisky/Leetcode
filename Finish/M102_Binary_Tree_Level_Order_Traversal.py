# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        ans = []
        
        if not root:
            return []
        queue = [root]
        tmp = []
        l = []
        while queue:
            node = queue.pop(0)
            l.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            
            if not queue:
                ans.append(l)
                l = []
                queue, tmp = tmp, []
        
        return ans