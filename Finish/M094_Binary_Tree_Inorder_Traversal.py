# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ## iterative
        ans = []
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            node = stack.pop()
            ans.append(node.val)
            root = node.right

        ## recursive
        ans = []
        def goLeft(root, ans):
            if not root:
                return
            goLeft(root.left, ans)
            ans.append(root.val)
            goLeft(root.right, ans)
        
        
        goLeft(root, ans)
        
        return ans