class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = {}
        ## Read
        for i,v in enumerate(equations):
            if v[0] not in dic:
                dic[v[0]] = []
            dic[v[0]].append([v[1], values[i]])
            if v[1] not in dic:
                dic[v[1]] = []
            dic[v[1]].append([v[0], 1/values[i]])
        print(dic)
        
        ## BFS
        def bfs(x, y):
            if x not in dic or y not in dic:
                return -1.0
            
            queue = [[x, 1.0]]
            visit = {}
            while queue:
                n, val = queue.pop(0)
                if n == y:
                    return val
                for item in dic[n]:
                    if item[0] not in visit:
                        queue.append([item[0], val*item[1]])
                        visit[item[0]] = 1
            return -1.0
            
        ## Implement
        ans = []
        for i, v in enumerate(queries):
            x, y = v
            ans.append(bfs(x,y))
            
        return ans
    
    
        
        