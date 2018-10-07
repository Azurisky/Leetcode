class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        tmp = x ^ y
        count = 0
        while tmp:
            tmp &= (tmp-1)
            count += 1
        
        return count