# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

## 99%, save the current
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.item = iterator
        self.hasN = iterator.hasNext()
        self.cur = None
        
        if self.hasN:
            self.cur = self.item.next()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        ans = self.cur
        
        return ans

    def next(self):
        """
        :rtype: int
        """
        ans = self.cur
        self.hasN = self.item.hasNext()
        self.cur = self.item.next()
        
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.hasN

## 10%
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.prev = 0
        self.item = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        tmp = []
        count = 0
        while self.item.hasNext():
            if count == 0:
                ans = self.item.next()
                tmp.append(ans)
            else:
                tmp.append(self.item.next())
            count += 1
        self.item = Iterator(tmp)
        return ans

    def next(self):
        """
        :rtype: int
        """
        ans = self.item.next()
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.item.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].