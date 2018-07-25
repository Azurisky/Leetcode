class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        l = len(s)-1
        for i in s:
            ans += (26 ** l) * (ord(i) - ord('A') + 1)
            l -= 1
        
        return ans
        