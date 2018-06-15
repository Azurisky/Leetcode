class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        ## 98%
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return ["{}->{}".format(lower, upper)]
        i = 0
        ans = []
        l , u = nums[0], nums[-1]
        while i < len(nums) and  nums[i] <= upper:
            if nums[i] > lower:
                if nums[i] - lower > 1:
                    ans.append("{}->{}".format(lower, nums[i]-1))
                elif nums[i] - lower == 1:
                    ans.append("{}".format(lower))
                lower = nums[i] + 1
            elif nums[i] == lower:
                lower += 1
                i += 1
            else:
                i += 1
            # print(lower, ans)
        # print(lower, upper)
        if lower == upper:
            ans.append("{}".format(upper))
        elif lower < upper+1:
            ans.append("{}->{}".format(lower, upper))
        return ans