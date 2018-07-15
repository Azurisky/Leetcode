class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        ## Do it in one-pass, using only O(1) extra memory and without modifying the value of the board
        if not board:
            return 0
        l = len(board)
        c = len(board[0])
        ans = 0
        for i in range(l):
            for j in range(c):
                if board[i][j] == 'X':
                    ans += 1
                    if (i-1 > -1 and board[i-1][j] == 'X') or (j-1 > -1 and board[i][j-1] == 'X'):
                        ans -= 1
                        # print(i, j)
        
        return ans