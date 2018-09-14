class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## https://leetcode.com/problems/rotate-array/discuss/54426/Summary-of-solutions-in-Python
        
        def reverse(nums, i, j):
            while j > i:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        l = len(nums)
        if k > l:
            k = k%l
        reverse(nums, l-k, l-1)
        reverse(nums, 0, l-k-1)
        reverse(nums, 0, l-1)
        
                