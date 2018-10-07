class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        queue = []
        visited = {}
        for i in range(len(graph)):
            queue.append(i)
            visited[i] = visited.get(i, 0)
            while queue:
                node = queue.pop(0)
                if visited[node] == 0:
                    tmp = 1
                else:
                    tmp = 0

                for i in graph[node]:
                    if i not in visited:
                        visited[i] = tmp
                        queue.append(i)
                    else:
                        if visited[node] == visited[i]:
                            return False
                    
        return True
                