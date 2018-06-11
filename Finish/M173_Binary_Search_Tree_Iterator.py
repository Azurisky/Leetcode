# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

## Faster, handle in the beginning
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.handle(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return not not self.stack
        
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.handle(node.right)
        return node.val
        
    def handle(self, node):
        while node:
            self.stack.append(node)
            node = node.left

## 50.3%
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        
    def fill_stack(self):
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.root or not self.stack:
            self.fill_stack()
        if not self.stack:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        if not self.stack:
            self.fill_stack()
        ans = self.stack.pop()
        self.root = ans.right
        return ans.val
            
        

