class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        ## dp
        dp = [[1 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
        
        ## math 
        ans = 0
        def factorial(num):
            tmp = 1
            if num == 0 :
                return 1
            for i in range(1, num+1):
                tmp *= i
            return tmp
        
        ans = factorial(m-2+n)  / factorial(m-1) / factorial(n-1)
        
        return int(ans)