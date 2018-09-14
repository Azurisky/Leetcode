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
        