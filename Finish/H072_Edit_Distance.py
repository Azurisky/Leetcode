class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        # Use map to be faster
        a, b = len(word1)-1, len(word2)-1
        mem = {}
        
        def dist(a, b):
            if a == -1:
                return b+1
            if b == -1:
                return a+1
            if (a,b) in mem:
                return mem[(a,b)]
            if word1[a] == word2[b]:
                d = dist(a-1, b-1)
            else:
                d = min(dist(a-1, b-1), dist(a-1, b), dist(a, b-1)) + 1
            mem[(a,b)] = d
            return d
        
        return dist(a,b)


        # T(m,n) = S(m,n) = O(m*n)
        m, n = len(word1), len(word2)
        dp = list(range(n+1))
        for i in range(1, m+1):
            prev, dp[0] = dp[0], i
            for j in range(1, n+1):
                tmp = dp[j]
                dp[j] = min(
                    prev + int(word1[i-1] != word2[j-1]),
                    dp[j] + 1,
                    dp[j-1] + 1
                )
                prev = tmp
        return dp[-1]
        
        
        # T(m,n) = O(m*n)
        # S(m,n) = O(n)
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for j in range(n+1):
            dp[0][j] = j
        for i in range(m+1):
            dp[i][0] = i
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(
                    dp[i-1][j-1]+int(word1[i-1] != word2[j-1]),
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                )
        return dp[-1][-1]