class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        ## Faster
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
    
        ## Follow up
        for i in range(len(matrix[0]) - 1):
            tmp = matrix[0][i]
            for j in range(1, len(matrix)):
                if i+j < len(matrix[0]) and matrix[j][i+j] != tmp:
                    return False
        for i in range(1, len(matrix)-1):
            tmp = matrix[i][0]
            for j in range(i+1, len(matrix)):
                if j-i < len(matrix[0]) and matrix[j][j-i] != tmp:
                    return False
        return True