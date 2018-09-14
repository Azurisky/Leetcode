class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        
        prev = 0
        ans = 0
        for i in range(len(s)-1, -1, -1):
            num = romans[s[i]]
            if prev > num:
                ans -= num
            else:
                ans += num
            prev = num
        return ans