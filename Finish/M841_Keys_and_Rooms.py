class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        ## Faster
        s, stack = set(range(1, len(rooms))), [0]
        while stack: 
            r = stack.pop()
            s.discard(r)
            for k in rooms[r]:
                if k in s: stack.append(k)
        return not s
        
        ## BFS
        if not rooms:
            return True
        queue = [0]
        r = [0]
        tmp = []
        while queue:
            key = queue.pop()
            if key not in r:
                r.append(key)
            for i in rooms[key]:
                if i not in r and i not in tmp:
                    tmp.append(i)
            if not queue:
                queue, tmp = tmp, []
        
        if len(r) == len(rooms):
            return True
        return False