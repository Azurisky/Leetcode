class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Split to left * right
        dp = [0] * max((n+1), 3)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        if n <= 2:
            return dp[n]
        start = 3
        while start <= n:
            i = 0
            j = start - 1
            tmp = 0
            while i < start and j >= 0:
                tmp += dp[i] * dp[j]
                dp[start] = tmp
                i += 1
                j -= 1
            start += 1
        
        return dp[-1]