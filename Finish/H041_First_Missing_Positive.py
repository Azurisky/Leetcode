class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## O(n) time and O(1) space
        if not nums:
            return 1
        nums.append(0)
        l = len(nums)
        for i, v in enumerate(nums):
            if v >= l or v < 0:
                nums[i] = 0
        for i in range(l):
            nums[nums[i]%l] += l
            
        for i in range(1, l):
            if nums[i] // l == 0:
                return i
        return l
        
        
        ## Not O(n) time
        if not nums:
            return 1
        count = 0
        for i, v in enumerate(nums):
            if v > 0:
                count += 1
        print(count)
        
        for i in range(1, count+1):
            if i not in nums:
                return i
        return i+1