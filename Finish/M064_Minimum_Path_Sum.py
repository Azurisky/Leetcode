class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[grid[j][i] for i in range(len(grid[0]))] for j in range(len(grid))]
        
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]
        
        for j in range(1, len(grid)):
            grid[j][0] += grid[j-1][0]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        # print(dp)
        
        return grid[-1][-1]