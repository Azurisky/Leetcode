class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        x = len(grid[0])
        y = len(grid)
        count = 0
        for i in range(y):
            for j in range(x):
                if grid[i][j] == '1':
                    count += 1
                    self.test(i, j, x, y, grid)
        return count
        
    def test(self, i, j, x, y, grid):
        if grid[i][j] == '1':
            grid[i][j] = '2'
            if i+1 < y:
                self.test(i+1, j, x, y, grid)
            if j+1 < x:
                self.test(i, j+1, x, y, grid)
            if i-1 >= 0:
                self.test(i-1, j, x, y, grid)
            if j-1 >= 0:
                self.test(i, j-1, x, y, grid)