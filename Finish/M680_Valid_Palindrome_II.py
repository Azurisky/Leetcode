class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        left = 0
        right = len(s)-1
        
        while right > left:
            if s[right] != s[left]:
                one = s[left:right]
                two = s[left+1:right+1]
                return one == one[::-1] or two == two[::-1] 
            right -= 1
            left += 1
        return True
            