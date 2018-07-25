class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for i in range(n)] for j in range(m)]
        
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            if dp[i-1][0] == 0 or obstacleGrid[i][0] == 1:
                    dp[i][0] = 0
        for j in range(1, n):
            if dp[0][j-1] == 0 or obstacleGrid[0][j] == 1:
                    dp[0][j] = 0
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        # print(dp)
        return dp[-1][-1]