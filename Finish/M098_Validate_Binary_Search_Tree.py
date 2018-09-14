# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ## Min and Max 
        def isBSTUtil(node, mini, maxi):
            # An empty tree is BST
            if node is None:
                return True
            
            # False if this node violates min/max constraint
            if node.val < mini or node.val > maxi:
                return False

            # Otherwise check the subtrees recursively
            # tightening the min or max constraint
            return (isBSTUtil(node.left, mini, node.val -1) and
                  isBSTUtil(node.right, node.val+1, maxi))
        
        return (isBSTUtil(root, float('-inf'), float('inf')))
        
        
        ## Better, store the node
        def isBSTHelper(node, l, r):
            if not node:
                return True
            if l != None and node.val <= l.val:
                return False
            if r != None and node.val >= r.val:
                return False
            
            return isBSTHelper(node.left, l, node) and isBSTHelper(node.right, node, r)
        
        return isBSTHelper(root, None, None)


    