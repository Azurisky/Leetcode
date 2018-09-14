class ZigzagIterator(object):
    
    ## Use generator and pointer, O(1) space
    def __init__(self, v1, v2):
        self.vals = (v[i] for i in itertools.count() for v in (v1, v2) if i < len(v))
        self.n = len(v1) + len(v2)
        print(self.vals)
        
    def next(self):
        self.n -= 1
        return next(self.vals)

    def hasNext(self):
        return self.n > 0
    
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.flag = 0
        self.limit = 2
        self.source = {}
        if v1:
            self.source[0] = v1
        if v2:
            self.source[1] = v2

    def next(self):
        """
        :rtype: int
        """
        # print(self.source)
        while self.flag not in self.source:
            self.flag += 1
            if self.flag >= self.limit:
                self.flag = 0
        # print(self.source[self.flag], self.flag)
        val = self.source[self.flag].pop(0)
        if not self.source[self.flag]:
            self.source.pop(self.flag, None)
        
        if self.source:
            self.flag += 1
            if self.flag >= self.limit:
                self.flag = 0
            while self.flag not in self.source:
                self.flag += 1
                if self.flag >= self.limit:
                    self.flag = 0
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.source:
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())