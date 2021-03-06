class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(1, l):
            if i%2 == 1 and nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            elif i%2 == 0 and nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        