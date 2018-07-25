# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
        
    
    def serialize(self, root):
        preorder = ''
        if not root:
            preorder += ',None'
            return preorder
        preorder += ','+str(root.val)
        preorder += self.serialize(root.left)
        preorder += self.serialize(root.right)
        return preorder

    def deserialize(self, encode_data):
        print(encode_data)
        pos = -1
        data = encode_data[1:].split(',')
        for i in range(len(data)):
            if data[i] == 'None':
                data[i] = None
            else:
                data[i] = int(data[i])
        root, count = self.buildTree(data, pos)
        return root

    def buildTree(self, data, pos):
        pos += 1
        if pos >= len(data) or data[pos]==None:
            return None, pos

        root = TreeNode(data[pos])
        root.left, pos = self.buildTree(data, pos)
        root.right, pos = self.buildTree(data, pos)
        return root, pos

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
        
#         l = []
#         queue = [root]
#         tmp = []
#         while queue:
            
#             n = []
#             node = queue.pop()
#             if not node.left:
#                 n.append("None")
#             else:
#                 tmp.append(node.left)
#                 n.append(str(node.left.val))
#             n.append(str(node.val))
#             if not node.right:
#                 n.append("None")
#             else:
#                 tmp.append(node.right)
#                 n.append(str(node.right.val))
#             l.append("-".join(n))
            
#             if not queue:
#                 queue, tmp = tmp, []
#         print(":".join(l))
#         return ":".join(l)
            

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         dic = {}
#         data = data.split(":")
#         print(data)
#         for i in data:
#             tmp = i.split('-')
#             r = int(i[1])
#             dic[r] = TreeNode(r)
#             if i[0] != 'None':
#                 dic[r].left =
             
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))