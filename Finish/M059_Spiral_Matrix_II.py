class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ## Cleaner
        if (n == 0):
            return []
        rowLength = n
        columnLength = n
        OutPut = [[0 for i in range(n)] for j in range(n)] 
        num = 1
        times = int(rowLength + 1 / 2)
        
        for i in range(times):
            for column in range(i, columnLength - i):
                OutPut[i][column] = num
                num += 1
            for row in range(i + 1, rowLength - i):
                OutPut[row][rowLength - i - 1] = num
                num += 1
            for columnSecond in range(columnLength - i - 2, i - 1, -1):
                OutPut[rowLength - i - 1][columnSecond] = num
                num += 1
            for rowSecond in range(rowLength - i - 2, i, -1):
                OutPut[rowSecond][i] = num
                num += 1
        return OutPut
                
        ## Pass
        if not n:
            return []
        if n == 1:
            return [[1]]
        l, r = 0, n
        u, d = 1, n
        ans = [[0 for i in range(n)] for j in range(n)]
        i, j = 0, 0
        di = 0
        count = 0
        while ans[i][j] == 0:
            count += 1
            if di == 0 and j+1 < r:
                ans[i][j] += count
                j = j+1
            elif di == 0 and j+1 == r:
                ans[i][j] += count
                i += 1
                r -= 1
                di = 1
            elif di == 1 and i+1 < d:
                ans[i][j] += count
                i = i+1
            elif di == 1 and i+1 == d:
                ans[i][j] += count
                j -= 1
                d -= 1
                di = 2
            elif di == 2 and j-1 >= l:
                ans[i][j] += count
                j = j-1
            elif di == 2 and j-1 < l:
                ans[i][j] += count
                i -= 1
                l += 1
                di = 3
            elif di == 3 and i-1 >= u:
                ans[i][j] += count
                i = i-1
            elif di == 3 and i-1 < u:
                ans[i][j] += count
                j += 1
                u += 1
                di = 0
        return ans