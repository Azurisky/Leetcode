class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        ## Right Answer
        n = len(nums)
        for i, num in enumerate(nums):
            pos = num > 0               # direction of movements
            j = (i + num) % n           # take the first step
            steps = 1
            while steps < n and nums[j] % n != 0 and (nums[j] > 0) == pos:
                j = (j + nums[j]) % n   # take the next step
                steps += 1
            if steps == n:              # loop is found
                return True
            nums[i] = 0
            j = (i + num) % n           # set everything visited to zero to avoid repeating
            while nums[j] % n != 0 and (nums[j] > 0) == pos:
                j, nums[j] = (j + nums[j]) % n, 0

        return False
        
        
        ## Weird Question
        if not nums:
            return False
        visit = [0 for i in nums]
        pos = 0
        l = 0
        flag = 1
        if visit[0] < 0:
            flag = -1
        while True:
            l += 1
            pos += nums[pos]
            
            if pos >= len(nums):
                pos -= len(nums)
            elif pos < 0:
                pos += len(nums)
            if nums[pos] * flag < 0:
                return False
            if visit[pos] != 0:
                break
            visit[pos] = l
        
        if l - visit[pos] > 2:
            return True
        else:
            return False