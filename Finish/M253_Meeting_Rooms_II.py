# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals or len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        end = [] 
        start = []
        
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        i, j = 0 , 0
        start.sort()
        end.sort()
        ans = empty = 0
        while i < len(intervals) and j < len(intervals):
            if start[i] < end[j]:
                i += 1
                if empty == 0:
                    ans += 1
                else:
                    empty -= 1
            else:
                empty += 1
                j += 1
        return ans