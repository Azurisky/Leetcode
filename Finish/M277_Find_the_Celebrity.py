# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = 0
        for i in range(1, n):
            if knows(tmp, i):
                tmp = i
        for i in range(n):
            if i != tmp and knows(tmp, i):
                return -1
        for i in range(n):
            if i != tmp and not knows(i, tmp):
                return -1
        return tmp
                
        