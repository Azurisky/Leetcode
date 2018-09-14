class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        ## Easy
        l = len(nums)
        b = -1
        w = -1
        r = -1
        for i in range(l):
            if nums[i] == 2:
                b += 1
                nums[b] = 2
            elif nums[i] == 1:
                w += 1
                b += 1
                nums[b] = 2
                nums[w] = 1
            else:
                r += 1
                w += 1
                b += 1
                nums[b] = 2
                nums[w] = 1
                nums[r] = 0
            
        ## Swap
        l = len(nums)
        b = l-1
        w = 0
        r = 0
        while w <= b:
            if nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            elif nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
            else:
                w += 1
                
            
            