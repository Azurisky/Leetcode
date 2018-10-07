class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        ## Union Find
        dic = {}
        
        def findParent(num):
            if num != dic[num]:
                dic[num] = findParent(dic[num])
            return dic[num]
        
        for i, j in edges:
            if i in dic and j in dic:
                if findParent(i) == findParent(j):
                    ans = [i, j]               
            if i in dic:
                tmp1 = findParent(i)
            else:
                dic[i] = i
                tmp1 = i
                
            if j in dic:
                tmp2 = findParent(j)
                dic[tmp2] = tmp1
            else:
                dic[j] = tmp1
            
        return ans

        ## Find

        def find(val):
            if val not in parent:
                parent[val] = val
            if val != parent[val]:
                parent[val] = find(parent[val])
            return parent[val]
        
        parent = {}
        group = {}
        for (x, y) in edges:
            # print(parent)
            # print(group)
            if x not in parent and y not in parent:
                parent[x] = x
                parent[y] = x
                group[x] = [x, y]
            elif x not in parent:
                r = parent[y]
                parent[x] = r
                group[r] += [x]
            elif y not in parent:
                r = parent[x]
                parent[y] = r
                group[r] += [y]
            else:
                px = parent[x]
                py = parent[y]
                if px == py:
                    return [x, y]
                else:
                    if len(group[px]) > len(group[py]):
                        px, py = py, px
                    for node in group[px]:
                        parent[node] = py
                        group[py].append(node)
                    group.pop(px, None)
        return []
        
        ## Union find
        ans = []
        parent = {}
        def find(val):
            if val not in parent:
                parent[val] = val
            if val != parent[val]:
                parent[val] = find(parent[val])
            return parent[val]
        
        for (x, y) in edges:
            if find(x) == find(y):
                # print(parent)
                return [x, y]
            else:
                parent[find(x)] = find(y)
        # print(parent)
        return []
        