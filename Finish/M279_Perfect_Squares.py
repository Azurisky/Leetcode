class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## DP
        if n == int(n**0.5):
            return 1
        dp = [i for i in range(n+1)]
        square = [i**2 for i in range(int(n**0.5)+1)]
        for i in range(1,n+1):
            for item in square:
                if i-item<0:
                    break
                else:
                    dp[i] = min(dp[i],dp[i-item]+1)
       return dp[n]

        ## BFS
        count = 1
        l = []
        while count ** 2 <= n:
            l.append(count ** 2)
            count += 1
        
        queue = [n]
        tmp = []
        level = 1
        while queue:
            num = queue.pop()
            for i in l:
                if i > num:
                    continue
                if i == num:
                    return level
                if i < num:
                    tmp.append(num-i)
            if not queue:
                queue, tmp = tmp, []
                level += 1
    
            
            