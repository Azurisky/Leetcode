# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ## Fastest, sort directly
        s, e = [], []
        
        for interval in intervals:
            start, end = interval.start, interval.end
            s.append(start)
            e.append(end)
        
        s.append(newInterval.start); s.sort()
        e.append(newInterval.end); e.sort()
        
        i = 0
        res = []
        while i < len(s):
            start, end = s[i], e[i]
            while i + 1 < len(s) and s[i + 1] <= e[i]:
                i += 1
                end = e[i]
            res.append(Interval(start, end))
            i += 1
        
        return res

        ## 88% 
        left = []
        right = []
        start = newInterval.start
        end = newInterval.end
        i = 0
        while i < len(intervals):
            if intervals[i].end < newInterval.start:
                left.append(intervals[i])
                i += 1
            elif intervals[i].start > newInterval.end:
                right.append(intervals[i])
                i += 1
            else:
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
                i += 1
            
        return left + [Interval(start, end)] + right
        