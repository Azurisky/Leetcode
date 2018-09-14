class Solution(object):
    
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from heapq import heappush, heappop
        dic = {}
        for i in tasks:
            dic[i] = dic.get(i, 0)
            dic[i] += 1
        
        ans = 0
        pq = []
        
        for i in dic:
            heappush(pq, (-1*dic[i], i))
        
        while pq:
            i, temp = 0, []
            while i <= n:
                ans += 1
                if pq:
                    x,y = heappop(pq)
                    if x != -1:
                        temp.append((x+1,y))
                if not pq and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(pq, item)
        return ans
            