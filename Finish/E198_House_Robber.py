class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        dp = [0]* (l+1)
        for i in range(l):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        print(dp)
        return dp[l-1]