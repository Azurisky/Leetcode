class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        l = len(nums)
        dp1 = [0]* (l)
        dp2 = [0]* (l)
        for i in range(l-1):
            dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])
        print(dp1)
        
        for i in range(1, l):
            dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])
        print(dp2)
        return max(dp1[l-2], dp2[l-1])