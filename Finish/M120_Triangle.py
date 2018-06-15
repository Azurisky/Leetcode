class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0]* (len(triangle)+1)
        tmp = [0]* (len(triangle)+1)
        # count = 0
        for i in range(len(triangle)-1, -1, -1):
            print(dp)
            for j, v in enumerate(triangle[i]):
                tmp[j] = min(dp[j], dp[j+1]) + v
            
            dp, tmp = tmp, [0]* (len(triangle)+1)
        return dp[0]