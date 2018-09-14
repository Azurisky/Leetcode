# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = [root]
        ans = []
        while s:
            node = s.pop()
            if node:
                ans.append(node.val)
                s.append(node.right)
                s.append(node.left)
        
        return ans
        
        ## iteration, like inorder
        s = []
        curr = root
        ans = []
        while s or curr:
            if curr:
                s.append(curr)
                ans.append(curr.val)
                curr = curr.left
            else:
                if s:
                    node = s.pop()
                    curr = node
                    curr = curr.right
            
        
        return ans
    
            
        