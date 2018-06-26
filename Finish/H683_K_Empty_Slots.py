class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        ## 95%
        def searchInterval(interals, pos):
            start, end = 0, len(intervals)-1
            while start <= end:
                mid = (start + end)//2
                if intervals[mid][0] <= pos and intervals[mid][1]>=pos:
                    return mid
                elif intervals[mid][0] > pos:
                    end = mid-1
                else:
                    start = mid+1
            return -1
        
        bloomPos = [0] * (len(flowers)+1)
        for day, pos in enumerate(flowers):
            bloomPos[day+1] = pos
        
        intervals = [[1, len(flowers)]]
        for day in range(1, len(flowers) + 1):
            pos = bloomPos[day]
            
            # 1. search for interval to break
            i = searchInterval(intervals, pos)
            if i == -1:
                continue
                
            start, end = intervals.pop(i)
            
            # 2. validate
            if day >= 2:
                if (pos - start == k and start != 1) or (end != len(flowers) and end - pos == k):
                    return day

            # 3. break the interval and add candidate interval back in
            if end - pos > k:
                intervals.insert(i, [pos+1, end])
            if pos- start >k:
                intervals.insert(i, [start, pos-1])   
        return -1


        # Passed, 88%
        l = len(flowers)
        new = [0] * (l+1)
        for i in range(l):
            new[flowers[i]-1] = i
        # print(new[1:])
        flowers = new
        if k > l - 2 or k < 0: 
            return -1
            
        cur = 0
        ans = -1
        for i in range(l):
            end = cur+k+1
            if end >= l:
                continue
            if i == end:
                v = max(flowers[cur], flowers[end])+1
                if ans < 0 or v < ans:
                    ans = v
            if flowers[i] < flowers[cur] or flowers[i] < flowers[end]:
                cur = i
        return ans


        ## TLE
        l = len(flowers)
        new = [0] * (l+1)
        for i in range(l):
            new[flowers[i]] = i+1
        # print(new[1:])
        flowers = new[1:]
        ans = []
        for i, v in enumerate(flowers):
            if i+k+1 < l:
                m = max(flowers[i], flowers[i+k+1])
                # print(m)
                count = 0
                for j in flowers[i+1:i+k+1]:
                    if j <= m:
                        break
                    else:
                        count += 1
                if count == k:
                    ans.append(m)
        if ans:
            return min(ans)
        return -1
                