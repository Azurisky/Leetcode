class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        prices.append(0)
        hold = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if i > 0 and prices[i] < prices[i-1]:
                ans += prices[i-1] - hold
                hold = prices[i]
            print(hold, ans)
        return ans
        