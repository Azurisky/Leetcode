class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        ## Union Find

        dic = {}
        
        def findparent(num):
            if num != dic[num]:
                dic[num] = findparent(dic[num])
            return dic[num]
        
        for i, j in edges:
            if i in dic:
                tmp1 = findparent(i)
            else:
                dic[i] = i
                tmp1 = i
            
            if j in dic:
                tmp2 = findparent(j)
                dic[tmp2] = tmp1
            else:
                dic[j] = tmp1
        print(dic)
        ans = []
        for i in range(n):
            if i not in dic:
                ans.append(i)
            else:
                tmp = findparent(i)
                if tmp not in ans:
                    ans.append(tmp)
        
        return len(ans)

        ## Graph
        visited = {}
        nei = {}
        ans = 0
        for i in range(n):
            nei[i] = []
        for x, y in edges:
            nei[x].append(y)
            nei[y].append(x)
            
        def dfs(val):
            visited[val] = 1
            for j in nei[val]:
                if j not in visited:
                    dfs(j)
            
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        
        return ans
    
        
## Union Find    
class UnionFind(object):
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.count = 0
        for i in range(n):
            self.parent[i] = i
            self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(n)
        for edge in edges:
            u, v = edge[0], edge[1]
            uf.union(u, v)
        return uf.count
                    