class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        i = len(matrix) - 1
        j = 0
        
        while i >= 0 and j < n:
            # print(i, j)
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        
        return False
        
        
        