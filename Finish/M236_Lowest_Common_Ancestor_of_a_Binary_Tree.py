# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q    

        ## Myself
        dic = {}
        queue = [root]
        level = 0
        dic[root] = [None, 0]
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    dic[node.left] = [node, level+1]
                    tmp.append(node.left)
                if node.right:
                    dic[node.right] = [node, level+1]
                    tmp.append(node.right)
            queue, tmp = tmp, []
            level += 1
     
        depth_p = dic[p][1]
        depth_q = dic[q][1]
        while p != q:
            if depth_p > depth_q:
                p = dic[p][0]
                depth_p -= 1
            elif depth_p < depth_q:
                q = dic[q][0]
                depth_q -= 1
            else:
                p = dic[p][0]
                q = dic[q][0]
                depth_p -= 1
                depth_q -= 1
        return p