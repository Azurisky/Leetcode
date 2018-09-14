class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        hold, no_hold, cool = float('-inf'), 0, float('-inf')
        for i in prices:
            hold, no_hold, cool = max(hold, no_hold - i), max(cool, no_hold), hold + i
        return max(no_hold, cool)