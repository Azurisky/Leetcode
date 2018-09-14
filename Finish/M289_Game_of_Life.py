class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        
        # calculate the number of live neighbors for cell (i,j)
        def findLiveNeighbor(board, i, j):
            count = 0
            for a,b in [(i-1,j-1),(i-1,j),(i-1,j+1),(i+1,j-1),(i+1,j),(i+1,j+1),(i,j-1),(i,j+1)]:
                if a >= 0 and a < len(board) and b >= 0 and b < len(board[0]) and board[a][b] % 2 == 1:
                    count += 1
            return count        
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                liveNeighbors = findLiveNeighbor(board, i, j)
                if board[i][j] == 0 and liveNeighbors == 3 or board[i][j] == 1 and liveNeighbors in [2,3]:
                        board[i][j] |= 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1
        return