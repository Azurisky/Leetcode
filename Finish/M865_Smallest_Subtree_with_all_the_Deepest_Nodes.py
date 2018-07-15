# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ## 100%
        dic = {}
        deep = {}
        queue = {root}
        tmp = []
        count = 0
        while queue:
            node = queue.pop()
            deep[node] = count
            if node.left:
                tmp.append(node.left)
                dic[node.left] = node
            if node.right:
                tmp.append(node.right)
                dic[node.right] = node
            if not queue:
                count += 1
                queue, tmp = tmp, []
        
        l = []
        for i in deep:
            if deep[i] == count-1:
                l.append(i) 
        while len(l) > 1:
            tmp = []
            for i in l:
                if dic[i] not in tmp:
                    tmp.append(dic[i])
            l = tmp
        return l[0]
        
            
        