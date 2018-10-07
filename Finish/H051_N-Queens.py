class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        ## https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
        res = []
        def dfs(queens, ddiff, ssum):
            p = len(queens)
            if p == n:
                queens = ['.' * i + 'Q' + '.' * (n - 1 - i) for i in queens]
                res.append(queens)
                # print(queens)
                return
            for q in range(n):
                if q in queens or p - q in ddiff or p + q in ssum: 
                    continue
                dfs(queens + [q],
                    ddiff + [p - q],
                    ssum + [p + q])
        dfs([], [], [])
        return res