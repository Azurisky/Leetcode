class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ## Use stack, 96%
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

        ## TLE
        ans = []
        def cal(heights):
            if not heights:
                ans.append(0)
                return
            if len(heights) == 1:
                ans.append(heights[0])
                return
            m = min(heights)
            ans.append(len(heights)*m)
            tmp = heights
            while m in tmp:
                i = tmp.index(m)
                cal(tmp[:i])
                tmp = tmp[i+1:]
            cal(tmp)
            return
        cal(heights)
        # print(ans)
        return max(ans)