# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def buildTree(val):
            if not val:
                return [None]
            elif len(val) == 1:
                return [TreeNode(val[0])]
            nodeList = []
            for i in range(len(val)):
                leftNode = buildTree(val[:i])
                rightNode = buildTree(val[i+1:])
                for l in leftNode:
                    for r in rightNode:
                        node = TreeNode(val[i])
                        node.left = l
                        node.right = r
                        nodeList.append(node)
                        
            return nodeList
            
        if n == 0:
            return []
        vals = [i for i in range(1,n+1)]
        
        return buildTree(vals)
        