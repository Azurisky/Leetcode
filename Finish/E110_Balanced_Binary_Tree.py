# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depthAndBalan(root):
            if root is None:
                return 1, True
            leftDep, leftBal = depthAndBalan(root.left)
            rightDep, rightBal = depthAndBalan(root.right)
            curBal = abs(leftDep - rightDep) <= 1
            return max(leftDep, rightDep)+1, leftBal and rightBal and curBal

        return depthAndBalan(root)[1]
        
        ## Normal balanced tree 
        if not root:
            return True
        queue = [root]
        tmp = []
        level = 0
        mini = 0
        flag = 1
        while queue:
            if level > mini + 1:
                return False
            node = queue.pop(0)
            if not node.left and not node.right and flag:
                flag = 0
                mini = level
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if not queue:
                queue, tmp = tmp, []
                level += 1
        return True
            
        