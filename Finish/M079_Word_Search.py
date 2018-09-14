class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        ## Pass
        def dfs(board, i, j, word):
            if len(word) == 0: # all the characters are checked
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
                return False
            tmp = board[i][j]  # first character is found, check the remaining part
            board[i][j] = "#"  # avoid visit agian 
            # check whether can find "word" along one direction
            res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) \
            or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
            board[i][j] = tmp
            return res
        
        
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False
    
        
        
        
        ## TLE
        def checkWord(index, i, j, d):
            # print(m, n, i, j)
            board[i][j] = " "
            ans = False
            if index == len(word):
                return True
            if i+1 < n and board[i+1][j] == word[index] and d != 1:
                ans |= checkWord(index+1, i+1, j, 2)
            if i-1 >= 0 and board[i-1][j] == word[index] and d != 2:
                ans |= checkWord(index+1, i-1, j, 1)
            if j+1 < m and board[i][j+1] == word[index] and d != 3:
                ans |= checkWord(index+1, i, j+1, 4)
            if j-1 >= 0 and board[i][j-1] == word[index] and d != 4:
                ans |= checkWord(index+1, i, j-1, 3)
            board[i][j] = word[index-1]
            return ans
        
        m = len(board[0])
        n = len(board)
        # if len(word) > m*n:
        #     return False
        # print(m, n)
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if len(word) == 0:
                        return True
                    else:
                        if checkWord(1, i, j, 0):
                            return True
        return False
        