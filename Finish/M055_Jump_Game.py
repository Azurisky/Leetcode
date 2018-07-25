class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        ## Going backwards
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal
        
        ## Going foward
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True

        ## use too much memory
        l = len(nums)
        cur = 0
        jump = nums[0]
        while jump:
            if cur + jump >= l-1:
                return True
            total = 0
            tmp = 0
            new = cur 
            for i in range(cur+1, cur+1+jump):
                if i < l and nums[i]+i >= total:
                    total = nums[i]+i
                    tmp = nums[i]
                    new = i
            jump = tmp
            cur = new
        return cur >= l-1       