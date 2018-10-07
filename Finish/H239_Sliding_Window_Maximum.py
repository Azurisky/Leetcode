
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ## Use dequ, pop out the smaller item on the fly
        from collections import deque
        d = deque()
        out = []
        for i, n in enumerate(nums):
            ## Pop out the samllr item
            while d and nums[d[-1]] < n:
                d.pop()
            d += i
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]]
        return out
        
        ## Use heap, faster
        from heapq import heappop, heappush
        
        if not nums:
            return []
        pq = []
        dic = {}
        for i in range(k-1):
            heappush(pq, -nums[i])
            dic[-nums[i]] = i
        ans = []
        
        for i in range(k-1, len(nums)):
            heappush(pq, -nums[i])
            dic[-nums[i]] = i
            while dic[pq[0]] < i-k+1:
                heappop(pq)
            ans.append(-pq[0])
        return ans
        
        ## Super slow
        ans = []
        for i in range(len(nums)-k+1):
            s = max(nums[i:i+k])
            ans .append(s)
        
        return ans