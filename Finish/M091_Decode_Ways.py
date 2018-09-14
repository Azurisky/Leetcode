class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## dp
        
        dp = [0 for i in range(len(s)+1)]
        if not s or s[0] == '0':
            return 0
        dp[0] = 1
        
        for i in range(1, len(s)+1):
            if s[i-1:i] != '0':
                dp[i] += dp[i-1]
            if i != 1 and '09' < s[i-2:i] <= '26':
                dp[i] += dp[i-2]
        # print(dp) 
        
        return dp[-1]