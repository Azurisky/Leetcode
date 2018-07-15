class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
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
        