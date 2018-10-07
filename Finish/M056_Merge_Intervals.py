# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        ## cleaner
        dic = {}
        start = []
        for i in intervals:
            dic[i.start] = dic.get(i.start, 0)
            dic[i.start] = max(i.end, dic[i.start])
            start.append(i.start)
        
        start.sort()
        ans = []
        for i in start:
            if ans and ans[-1][1] >= i:
                ans[-1][1] = max(ans[-1][1], dic[i])
            else:
                ans.append([i, dic[i]])  
        
        return ans


        ## normal 
        if not intervals:
            return []
        elif len(intervals) == 1:
            return intervals
        
        dic = {}
        start = []
        for i in intervals:
            dic[i.start] = dic.get(i.start, 0)
            dic[i.start] = max(i.end, dic[i.start])
            start.append(i.start)
        
        start.sort()
        s = start[0]
        e = dic[start[0]]
        index = 1
        l = len(start)
        ans = []
        while index < l:
            while index < l and start[index] <= e:
                e = max(e, dic[start[index]])
                index += 1
            ans.append([s, e])
            if index == l:
                return ans
            s = start[index]
            e = dic[start[index]]
        return ans

        ## best
        if not intervals:
            return []
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start = sorted(start)
        end = sorted(end)
        l = len(intervals)
        i, j = 0, 0
        ans = []
        
        while i < len(intervals):
            s = start[i]
            e = end[j]
            i += 1
            while i < l and j < l and e >= start[i]:
                i += 1
                j += 1
                e = end[j]
            ans.append([s, e])
            j += 1
        return ans
        