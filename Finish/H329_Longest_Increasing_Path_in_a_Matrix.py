class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ## Use map to store the prev result
        def dfs(matrix, i, j, prev, path):
            if i >= m or i < 0 or j >= n or j < 0 or matrix[i][j] <= prev:
                return 0
            
            # print(prev)
            if "{}, {}".format(i, j) in dic:
                return 1 + dic["{}, {}".format(i, j)]
            path += 1
            tmp = matrix[i][j]
            matrix[i][j] = float('-inf')
            up = dfs(matrix, i-1, j, tmp, path)
            down = dfs(matrix, i+1, j, tmp, path)
            left = dfs(matrix, i, j-1, tmp, path)
            right = dfs(matrix, i, j+1, tmp, path)
            matrix[i][j] = tmp
            ans = max(up, down, left, right)
            dic["{}, {}".format(i, j)] = ans
            return 1 + ans
        
        dic = {}
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(matrix, i, j, float('-inf'), 0))
        return ans

        ## TLE
        def dfs(matrix, i, j, prev, path):
            if i >= m or i < 0 or j >= n or j < 0 or matrix[i][j] <= prev:
                return 0
            
            # print(prev)
            path += 1
            tmp = matrix[i][j]
            matrix[i][j] = float('-inf')
            up = dfs(matrix, i-1, j, tmp, path)
            down = dfs(matrix, i+1, j, tmp, path)
            left = dfs(matrix, i, j-1, tmp, path)
            right = dfs(matrix, i, j+1, tmp, path)
            matrix[i][j] = tmp
            ans = max(up, down, left, right)
            return 1 + ans
        
        
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(matrix, i, j, float('-inf'), 0))
        return ans