class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0
        dic = {}
        m = len(grid[0])
        n = len(grid)
        
        def expand(i, j, path):
            if grid[i][j] == 1:
                path.append([i, j])
                grid[i][j] = 2
                if i+1 < n:
                    expand(i+1, j, path)
                if j+1 < m:
                    expand(i, j+1, path)
                if i-1 >= 0:
                    expand(i-1, j, path)
                if j-1 >= 0:
                    expand(i, j-1, path)
            return path
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # print(i, j)
                    tmp = expand(i, j, [])
                    i_min = float('inf')
                    j_min = float('inf')
                    for x, y in tmp:
                        i_min = min(x, i_min)
                        j_min = min(y, j_min)
                    for index in range(len(tmp)):
                        tmp[index][0] -= i_min
                        tmp[index][1] -= j_min
                    res = ''
                    for x, y in tmp:
                        res += str(x)+','+str(y)+'#'
                    # print(res)
                    if res not in dic:
                        dic[res] = 1
        return len(dic)
                    
            