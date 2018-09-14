class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        q, x, ans = n, 1, 0
        while q != 0:
            digits = q % 10
            q //= 10
            ans += q * x
            if digits == 1:
                ans += n%x + 1
            elif digits > 1:
                ans += x
            x *= 10
        return ans