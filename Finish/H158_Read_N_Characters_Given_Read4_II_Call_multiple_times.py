# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while True:
            buf4 = [""]*4
            l = read4(buf4)
            self.queue.extend(buf4)
            curr = min(len(self.queue), n-idx)
            for i in xrange(curr):
                buf[idx] = self.queue.pop(0)
                idx+=1
            if curr == 0:
                break 
        return idx