class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        dp = ['' for i in range(numRows)]
        if numRows == 1:
            return s
        count = 0
        flag = 1
        for i in s:
            dp[count] += i
            if count == 0:
                flag = 1
            elif count == numRows-1:
                flag = 0
            if flag:
                count += 1
            else:
                count -= 1
        return "".join(dp)