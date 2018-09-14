# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ## idea in two sum
    def helper(self, root, target, so_far, dic):
        if root:
            need = so_far + root.val - target
            if need in dic:
                self.result += dic[need]
            dic[so_far + root.val] = dic.get(so_far + root.val, 0)
            dic[so_far + root.val] += 1
            self.helper(root.left, target, so_far+root.val, dic)
            self.helper(root.right, target, so_far+root.val, dic)
            dic[so_far + root.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result
            