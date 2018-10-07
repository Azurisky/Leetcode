# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count, MAX_CHARS = 0, 4
        temp = [""] * MAX_CHARS
        while True:
            x = read4(temp)
            if count + x > n: 
                for i in range(n-count):
                    buf[count], count = temp[i], count + 1
                break
            elif x < 4:
                for i in range(x):
                    buf[count], count = temp[i], count + 1
                break
            else:
                for i in range(4):
                    buf[count], count = temp[i], count + 1
        return count