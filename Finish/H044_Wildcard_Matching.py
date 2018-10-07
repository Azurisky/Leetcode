class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        m = len(s)
        n = len(p)
        
        dp = [False for i in range(n+1)]
        
        dp[0] = True
        
        for i in range(1, n+1):
            dp[i] = dp[i-1] and p[i-1] == '*'
        # print(dp)
        for i in range(1, m+1):
            tmp = []
            for k in dp:
                tmp.append(k)
            dp = [False for l in range(n+1)]
            for j in range(1, n+1):
                # print(p[j-1], s[i-1])
                if p[j-1] != '*':
                    dp[j] = tmp[j-1] and (p[j-1] == s[i-1] or p[j-1] == '?')
                    # dp[j] = tmp[j-1] or tmp[j]
                else:
                    dp[j] = tmp[j-1] or tmp[j] or dp[j-1]
            # print(dp)
        
        return dp[-1]
                    
                    
                    
                    
                    
                    
                    