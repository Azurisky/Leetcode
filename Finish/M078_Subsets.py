class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## recusive
        ans = []
        def dfs(nums, index, path, ans):
            ans.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i+1, path+[nums[i]], ans)
        
        dfs(nums, 0, [], ans)
        return ans
        
        ## iterative
        ans = [[]]
        if not nums:
            return []
        for i in nums:
            tmp = []
            for j in ans:
                tmp.append(j+[i])
            ans += tmp
        return ans