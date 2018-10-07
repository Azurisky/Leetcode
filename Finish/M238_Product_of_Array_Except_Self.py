class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        ans = [1] * l
        tmp = 1
        for i in range(1, l):
            tmp *= nums[i-1]
            ans[i] *= tmp
        
        tmp = 1
        for i in range(l-2, -1, -1):
            tmp *= nums[i+1]
            ans[i] *= tmp
        
        return ans