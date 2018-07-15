class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## DP
        nums.sort()
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num > i:
                    continue
                dp[i] += dp[i-num]
        return dp[target]
        
        ## DFS, TLE
        ans = []
        def find(target, path):
            if target == 0:
                ans.append(path)
            for i, v in enumerate(nums):
                if target - v < 0:
                    continue
                find(target-v, path + [v])
        find(target, [])
        # print(ans)
        return len(ans)