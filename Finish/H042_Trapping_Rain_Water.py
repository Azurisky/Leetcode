class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r = 0, n-1
        m = 0
        ans = 0
        while l < r:
            while l < r and height[l] <= m:
                ans += m - height[l]
                l += 1
            while l < r and height[r] <= m:
                ans += m - height[r]
                r -= 1
            m = min(height[l], height[r])
        return ans
            