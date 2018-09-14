class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 
        ans = 0
        gap = float('inf')
        nums= sorted(nums)
        for i, v in enumerate(nums):
            head = i + 1
            tail = len(nums)-1
            while head < tail:
                tmp = v + nums[head] + nums[tail]
                # print(tmp)
                if tmp > target:
                    tail -= 1
                elif tmp < target:
                    head += 1
                else:
                    return target
                tmp_gap = abs(tmp-target)
                if tmp_gap <= gap:
                    ans = tmp
                    gap = tmp_gap
        
        return ans
                
            