class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dp = [0] * len(s)
        index = []
        stack = []
        ans = 0
        for i, v in enumerate(s):
            if v == '(':
                index.append(i)
                stack.append(v)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    ind = index.pop()
                    dp[i] = dp[ind-1] + (i-ind+1)
                    ans = max(ans, dp[i])
        # print(dp)
        return ans
                