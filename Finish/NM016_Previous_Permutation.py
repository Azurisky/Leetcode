class Solution:
    def PrevPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        index = l - 1
        while index > 0 and nums[index] >= nums[index-1]:
            index -= 1
        index -= 1
        # print(index)
        if index == -1:
            nums = nums.reverse()
            return 
        
        swap = l -1
        while nums[swap] >= nums[index]:
            swap -= 1
        
        nums[swap], nums[index] = nums[index], nums[swap]
        nums[index+1:] = nums[index+1:][::-1]
        