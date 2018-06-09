class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        count = 0
        
        for i in dic:
            if dic[i] % 2 == 1:
                count += 1
        
        return not (count > 1)