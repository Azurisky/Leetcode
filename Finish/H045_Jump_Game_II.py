class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Greedy
        if not nums or len(nums) == 1:
            return 0
        jump = nums[0]
        l = len(nums)
        pos = 0
        ma = 0
        tmp_pos = 0
        tmp_jump = 0
        ans = 0
        while jump + pos < l-1:
            for i, v in enumerate(nums[pos:pos+jump+1]):
                tmp = v + i + pos
                if tmp > ma:
                    ma = tmp
                    tmp_pos = i + pos
                    tmp_jump = v
            # print(ma, pos, tmp_jump)
            jump = tmp_jump
            pos = tmp_pos
            ans += 1
        return ans+1
        
            
        
                
            