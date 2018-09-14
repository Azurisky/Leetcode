class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.limit = len(vec2d)
        self.col = 0
        self.row = 0
        self.data = vec2d
        self.flag = True
        while self.row < self.limit and not self.data[self.row] :
            self.row += 1
        if self.row >= self.limit:
            self.flag = False

    def next(self):
        """
        :rtype: int
        """
        ans = self.data[self.row][self.col]
        self.col += 1
        if self.col >= len(self.data[self.row]):
            self.row += 1
            self.col = 0
            while self.row < self.limit and not self.data[self.row] :
                self.row += 1
            if self.row >= self.limit:
                self.flag = False
        return ans
                
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.flag
        
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())