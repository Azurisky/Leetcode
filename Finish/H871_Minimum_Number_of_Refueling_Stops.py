class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        ## O(n), use heap
        from heapq import heappush, heappop
        ans = 0
        cur = startFuel
        index = 0
        pq = []
        while cur < target:
            while index < len(stations) and cur >= stations[index][0]:
                heappush(pq, -stations[index][1])
                index += 1
            if pq:
                cur -= heappop(pq)
            else:
                return -1
            ans += 1
        return ans
        
        ## O(n**2), use dp
        dp = [0] * (len(stations)+1)
        dp[0] = startFuel
        # print(dp)
        for i, v in enumerate(stations):
            for j in range(i+1)[::-1]:
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j]+stations[i][1])
        # print(dp)
        for i, v in enumerate(dp):
            if v >= target:
                return i
        return -1
        