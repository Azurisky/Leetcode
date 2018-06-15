from heapq import heappush, heappop
class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        heap = [0]      
        if not grid or not grid[0]:
            return 0
        for i, k in enumerate(grid):
            for j, v in enumerate(k):
                if v == '0':
                    count = 0
                    tmp = j
                    while tmp < len(k):
                        if grid[i][tmp] == 'W':
                            break
                        elif grid[i][tmp] == 'E':
                            count -= 1
                        tmp += 1
                        
                    tmp = j
                    while tmp > -1:
                        if grid[i][tmp] == 'W':
                            break
                        elif grid[i][tmp] == 'E':
                            count -= 1
                        tmp -= 1
                    
                    tmp = i
                    while tmp < len(grid):
                        if grid[tmp][j] == 'W':
                            break
                        elif grid[tmp][j] == 'E':
                            count -= 1
                        tmp += 1
                    
                    tmp = i
                    while tmp > -1:
                        if grid[tmp][j] == 'W':
                            break
                        elif grid[tmp][j] == 'E':
                            count -= 1
                        tmp -= 1
                
                    heappush(heap, count)
            
        # print(heap)
        return -1*heap[0]
                