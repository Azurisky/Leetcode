class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        for e in nums:
            if count == 0:
                candidate, count = e, 1
            else:
                if candidate == e:
                    count += 1
                else:
                    count -= 1
        
        if count > 0 and nums.count(candidate) > len(nums)//2:
            return candidate 
        return None