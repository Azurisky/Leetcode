from heapq import heappop, heappush
class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.pq = []
        self.list = []
        self.id = 0
        self.pqd = {}       # id of items deleted in list but not pq
        self.listd = {}     # id of items deleted in pq but not list

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list.append([self.id, x])
        heappush(self.pq, [-x, -self.id])
        self.id += 1

    def pop(self):
        """
        :rtype: int
        """
        ans = self.top()
        self.pqd[self.list[-1][0]] = 1
        self.list.pop()
        return ans
       

    def top(self):
        """
        :rtype: int
        """
        while self.list[-1][0] in self.listd:
            self.listd.pop(self.list[-1][0], None)
            self.list.pop()
        return self.list[-1][1]


    def peekMax(self):
        """
        :rtype: int
        """
        while -self.pq[0][1] in self.pqd:
            self.pqd.pop(-self.pq[0][1], None)
            heappop(self.pq)
        return -self.pq[0][0]


    def popMax(self):
        """
        :rtype: int
        """
        ans = self.peekMax()
        nid = -heappop(self.pq)[1]
        self.listd[nid] = 1
        return ans


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()