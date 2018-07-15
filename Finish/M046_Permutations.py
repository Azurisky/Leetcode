class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        def dfs(nums, path):
            if not nums:
                ans.append(path)
            for i, v in enumerate(nums):
                dfs(nums[:i] + nums[i+1:], path + [v])
            
        dfs(nums, [])
        return ans
            