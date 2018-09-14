class Solution:
    def permuteUnique(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## Faster, O(n^3)
        if not num:
            return []
        num.sort()
        ret = [[]]
        for n in num:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    if i < l and seq[i] == n:
                        break
                    new_ret.append(seq[:i] + [n] + seq[i:])
            ret = new_ret
            # print(ret)
        return ret
        
        ## dfs, slow in this case O(n!)
        ans = []
        def dfs(nums, path):
            if not nums and path not in ans:
                ans.append(path)
            for i, v in enumerate(nums):
                dfs(nums[:i] + nums[i+1:], path + [v])
            
        dfs(nums, [])
        return ans
        
    ## Fast dfs
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        self.helper(res,nums,[])
        return res

    def helper(self, res, nums, path):
        if not nums:
            res.append(path)
            return
        dic = {x:1 for x in nums}

        for i in range(len(nums)):
            if dic[nums[i]] == 1:
                self.helper(res, nums[:i] + nums[i+1:], path + [nums[i]])
                dic[nums[i]] -= 1
            