class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.keymap = {}
        self.fremap = {}
        self.minfre = 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keymap:
            return -1
        else:
            node = self.keymap[key]
            node.fre += 1
            self.ddRemove(node)
            if self.fremap[self.minfre].next == self.fremap[self.minfre]:
                self.minfre += 1
            self.fremap[node.fre] = self.fremap.get(node.fre, DoubleListNode(None, None))
            root = self.fremap[node.fre]
            self.ddAddToTail(node, root)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0: return
        if key in self.keymap:
            self.keymap[key].value = value
            self.get(key)
        else:
            if len(self.keymap) == self.cap:
                root = self.fremap[self.minfre]
                keytbd = root.next.key
                self.ddRemove(root.next)
                del self.keymap[keytbd]
            node, self.minfre = DoubleListNode(key, value), 1
            self.fremap[self.minfre] = self.fremap.get(self.minfre, DoubleListNode(None, None))
            root = self.fremap[self.minfre]
            # root = self.fremap.setdefault(self.minfre, DoubleListNode(None, None))
            self.ddAddToTail(node, root)
            self.keymap[key] = node

                
    def ddRemove(self, node):
        n1, n2 = node.prev, node.next
        n1.next, n2.prev = n2, n1
        node.prev, node.next = None, None

        
    def ddAddToTail(self, node, tail):
        n1, n2 = tail.prev, tail
        node.prev, node.next = n1, n2
        n1.next, n2.prev = node, node

class DoubleListNode(object):
    def __init__(self, key, value):
        self.fre = 1
        self.key = key
        self.value = value
        self.prev = self
        self.next = self