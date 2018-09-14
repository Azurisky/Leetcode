class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            sign = 1
        else:
            x *= -1
            sign = -1
        
        ans = 0
        mul = 1
        while x != 0:
            ans *= 10
            ans += x%10 
            x //= 10
        if ans > 2**31: 
            return 0
        
        return ans * sign