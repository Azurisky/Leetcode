class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        list_squ = [[] for i in range(9)]
        list_col = [[] for i in range(9)]
        list_row = [[] for i in range(9)]
        print(list_col)
        
        for j, r in enumerate(board):
            for i, val in enumerate(r):
                # print(j, i, val)
                if val != ".":
                    if val in list_row[i] or val in list_col[j] or val in list_squ[3*(i//3) + (j//3)]:
                        return False
                    list_squ[3*(i//3) + (j//3)].append(val)
                    list_col[j].append(val)
                    list_row[i].append(val)
        return True