class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * 10001
        ma = 0
        for i in nums:
            if i > ma:
                ma = i
            dp[i] += i
        
        for i in range(ma+1):
            dp[i] = max(dp[i-1], dp[i]+dp[i-2])
            
        return dp[i]
        
        