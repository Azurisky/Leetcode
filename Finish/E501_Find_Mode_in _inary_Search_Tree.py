# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## No extra space
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack, count, prev, ma = self.find_all(root, [], [], 1, None, 1)

        return stack
        
    def find_all(self, root, stack, ans, count, prev, ma):
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            # ans.append(node.val)
            cur = node.val
            # print(ans, count, ma, prev, cur)
            if prev == cur:
                count += 1
            else:
                count = 1
            if count > ma:
                ans = [cur]
                ma = count
            if count == ma:
                if node.val not in ans:
                    ans.append(node.val)
            prev = cur
            if node.right:
                ans, count, prev, ma = self.find_all(node.right, stack, ans, count, node.val, ma)
            
        return ans, count, cur, ma

## Not good
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        stack = self.find_all(root, [], [])
        ans = []
        count = 1
        ma = 1
        dic = {}
        print(stack)
        for i in range(len(stack)):
            dic[stack[i]] = dic.get(stack[i], 0)
            dic[stack[i]] += 1
            if i < len(stack)-1:
                if stack[i] == stack[i+1]:
                    count += 1
                    ma = max(ma, count) 
                else:
                    count = 1
        
        for i in dic:
            if dic[i] == ma:
                ans.append(i)
        print(dic)
        print(ma)
        return ans
        
    def find_all(self, root, stack, ans):
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                self.find_all(node.right, stack, ans)
        return ans
    
        
        