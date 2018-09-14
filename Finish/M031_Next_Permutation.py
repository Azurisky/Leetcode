class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        ## idea from here, https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        if not nums:
        	return

        l = len(nums)
        i, j = l-2, l-1

        while i >= 0 and nums[i] >= nums[i+1]:
        	i -= 1

        if i == -1:
        	return nums.reverse()

        while j > i and nums[j] <= nums[i]:
        	j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]