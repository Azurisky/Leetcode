class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        l = len(nums)
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            x, y = i+1, l-1
            
            while y > x:
                s = nums[i] + nums[x] + nums[y]
                # print(s)
                if s == 0:
                    ans.append([nums[i], nums[x], nums[y]])
                    while y > x and nums[y] == nums[y-1]:
                        y -= 1
                    while y > x and nums[x] == nums[x+1]:
                        x += 1
                    y -= 1
                    x += 1
                elif s > 0:
                    y -= 1
                elif s < 0:
                    x += 1
        return ans
            
            