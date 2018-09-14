class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        
        ans = 0
        prices.append(0)
        l = len(prices)
        hold = prices[0]
        for i in range(1, l):
            print(ans, prices[i], hold)
            if prices[i] < prices[i-1] and prices[i-1] - hold > fee:
                ans += prices[i-1] - hold - fee
                ## trick here
                hold = prices[i-1] - fee
            if prices[i] < hold:
                hold = prices[i]
        return ans
                