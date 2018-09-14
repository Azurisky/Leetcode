class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        ## Use heap
        from heapq import heappush, heappop
        dic = {}
        for i in words:
            dic[i] = dic.get(i, 0)
            dic[i] += 1
        
        pq = []
        for i in dic:
            heappush(pq, [-dic[i], i])
        
        ans = []
        for j in range(k):
            c, key = heappop(pq)
            ans.append(key)
        
        return ans


        ## Use nothing
        dic = {}
        for i in words:
            dic[i] = dic.get(i, 0)
            dic[i] += 1
        
        bucket = [[] for i in range(len(words)+1)]
        
        for i in dic:
            bucket[dic[i]].append(i)
            
        res = []
        for i in reversed(range(len(words) + 1)):
            if len(res) >= k:
                break
            if len(bucket[i]) > 0:
                bucket[i].sort()
                if len(bucket[i]) + len(res) <= k:
                    res += bucket[i]
                else:
                    res += bucket[i][:k - len(res)]
        return res
                
            
            