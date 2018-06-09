from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = {}
        for i in tasks:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        ans, h = 0, []
        for i in dic:
            heappush(h, (-1*dic[i], i))
        # print(h)
        
        while h:
            i, temp = 0, []
            while i <= n:
                ans += 1
                if h:
                    x,y = heappop(h)
                    if x != -1:
                        temp.append((x+1,y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)
        return ans
                
            