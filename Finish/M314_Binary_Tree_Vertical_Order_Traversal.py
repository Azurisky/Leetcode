# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [[root, 0]]
        dic = {}
        mi, ma = 0, 0
        while stack:
            node, count = stack.pop(0)
            mi = min(mi, count)
            ma = max(ma, count)
            dic[count] = dic.get(count, [])
            dic[count] += [node.val]
            if node.left:
                stack.append([node.left, count-1])
            if node.right:
                stack.append([node.right, count+1])
        # print(dic)
        ans = []
        for i in range(mi, ma+1):
            if i in dic:
                ans.append(dic[i])
        return ans