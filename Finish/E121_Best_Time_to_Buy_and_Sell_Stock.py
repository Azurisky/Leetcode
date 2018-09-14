class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = 0
        ans = 0
        
        for i in prices[::-1]:
            if i > sell:
                sell = i
            else:
                if sell - i > ans:
                    ans = sell - i
        
        return ans
                