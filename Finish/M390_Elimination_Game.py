class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        ## Iterative
        start, count, step = 1, n, 1
        while count > 1:
            end = start + (count - 1) * step
            # compute the next round
            start = end - (count % 2) * step
            count /= 2
            step *= -2
        return start

        ## Recusive
        def helper(n, isLeft):
            if(n==1): return 1
            if(isLeft):
                return 2*helper(n//2, 0)
        # if started from left side the odd elements will be removed, the only remaining ones will the the even i.e.
        #       [1 2 3 4 5 6 7 8 9]==   [2 4 6 8]==     2*[1 2 3 4]
            elif(n%2==1):
                return 2*helper(n//2, 1)
        # same as left side the odd elements will be removed
            else:
                return 2*helper(n//2, 1) - 1
        # even elements will be removed and the only left ones will be [1 2 3 4 5 6 ]== [1 3 5]== 2*[1 2 3] - 1
            
        return helper(n, 1)