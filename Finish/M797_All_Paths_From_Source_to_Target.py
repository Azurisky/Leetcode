class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ## Recursive
        def move(index, q):
            if index == len(graph) - 1: 
                res.append(q)
            for i in graph[index]: 
                move(i, q + [i])
            return res
        
        res = []
        return move(0, [0])
        
        ## Iterative
        stack = []
        if not graph:
            return []
        ans = []
        stack.append([0, [0]])
        while stack:
            # print(stack)
            val, tmp = stack.pop()
            # print(tmp)
            if val == len(graph) -1:
                ans.append(tmp)
                continue
            for j in graph[val]:
                stack.append([j, tmp + [j]])
        return ans