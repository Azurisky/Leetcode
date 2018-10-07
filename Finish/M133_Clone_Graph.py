# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return 
        copy = UndirectedGraphNode(node.label)
        dic = {}
        dic[node] = copy
        queue = [node]
        while queue:
            node = queue.pop(0)
            for nei in node.neighbors: 
                if nei not in dic:
                    c = UndirectedGraphNode(nei.label)
                    dic[nei] = c
                    dic[node].neighbors.append(c)
                    queue.append(nei)
                else:
                    dic[node].neighbors.append(dic[nei])
        
        return copy
                