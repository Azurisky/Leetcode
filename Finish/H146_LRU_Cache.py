# 146. LRU Cache

class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            n = self.dict[key]
            self.remove(n)
            self.add(n)
            return n.value
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.remove(self.dict[key])
        n = Node(key, value)
        self.add(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.dict[n.key]
        return


    def add(self, node):
        p = self.tail.prev
        p.next = node 
        node.prev = p
        self.tail.prev = node
        node.next = self.tail


    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        
        



