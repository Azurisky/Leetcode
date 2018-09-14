class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from heapq import heappop, heappush
        
        ## O(klog(n))
        n = len(matrix)
        pq = []
        for i in range(n):
            heappush(pq, [matrix[i][0], i, 0])
        count = 0
        while count < k:
            tmp, index, col = heappop(pq)
            if col+1 < n:
                heappush(pq, [matrix[index][col+1], index, col+1])
            count += 1
            
        return tmp
            
                