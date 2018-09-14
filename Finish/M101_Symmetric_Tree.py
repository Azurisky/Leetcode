# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        ## recursive
        if not root:
            return True
        
        def isMirror(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            if left.val == right.val:
                outPair = isMirror(left.left, right.right)
                inPiar = isMirror(left.right, right.left)
                return outPair and inPair
            return False


        ## iteration
        if not root:
            return True
        queue = [root]
        tmp = []
        while queue:
            node = queue.pop(0)
            if node:
                tmp.append(node.left)
                tmp.append(node.right)
            
            if not queue:
                if tmp:
                    queue, tmp = tmp, []
                    l = len(queue)
                    # print(l)
                    if l%2 != 0:
                        return False
                    head = 0
                    tail = l-1
                    while head < tail:
                        if not queue[head] and not queue[tail]:
                            head += 1
                            tail -= 1
                        elif not queue[head] or not queue[tail]:
                            return False
                        elif queue[head].val != queue[tail].val:
                            return False
                        else:
                            head += 1
                            tail -= 1
                
        return True
        