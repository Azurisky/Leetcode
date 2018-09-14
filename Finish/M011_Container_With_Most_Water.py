class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height) - 1
        ans = 0
        while head <= tail:
            ans = max(min(height[head], height[tail])*(tail - head), ans)
            if height[head] > height[tail]:
                tail -= 1
            else:
                head += 1
        return ans