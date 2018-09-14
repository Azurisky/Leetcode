class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ## bucket sort O(n)
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)
            dic[num] += 1
        bucket = [[] for _ in range(len(nums)+1)]
        for key, val in dic.items():
            # val = dic[key]
            bucket[val].append(key)

        ret = []
        for row in reversed(bucket):
            if not row:
                continue
            else:
                for i in range(len(row)):
                    ret.append(row[i])
                    if len(ret) == k:
                        return ret
        
        ## heapq O(nlog(n))
        from heapq import heappush, heappop
        pq = []
        dic = {}
        ans = []
        for i in nums:
            dic[i] = dic.get(i, 0)
            dic[i] -= 1
        # print(dic)
        for i in dic:
            if [dic[i], i] not in pq:
                heappush(pq, [dic[i], i])
        for i in range(k):
            ans.append(heappop(pq)[1])
        return ans