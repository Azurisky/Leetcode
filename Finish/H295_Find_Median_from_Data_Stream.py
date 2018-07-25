from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.right:
            heappush(self.right, num)
            return 
        l = heappop(self.right)
        if num > l:
            heappush(self.right, num)
            heappush(self.left, -l)
        else:
            heappush(self.right, l)
            heappush(self.left, -num)
        
        while len(self.right) < len(self.left):
            heappush(self.right, -heappop(self.left))
        return 

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.right) == len(self.left):
            r = self.right[0]
            l = self.left[0]
            return (r-l)/2
        else:
            r = self.right[0]
            return r

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()