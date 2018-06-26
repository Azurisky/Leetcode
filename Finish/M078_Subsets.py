class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        if not nums:
            return []
        for i in nums:
            tmp = []
            for j in ans:
                tmp.append(j+[i])
            ans += tmp
        
        return ans