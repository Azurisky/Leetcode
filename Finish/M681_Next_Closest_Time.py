class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        ## Use min and hour better, 96%
        m, h = time[3:], time[:2]
        nums = list(set([n for n in m+h]))
        combs = set(nums[i]+nums[j] for i in range(len(nums)) for j in range(len(nums)))
        
        mins = [minute for minute in combs if m < minute < '60']
        hours = [hour for hour in combs if h < hour < '24']
        if mins:
            return h+':'+min(mins)
        elif hours:
            return min(hours)+':'+ min(combs)
        else:
            return min(combs) + ':' + min(combs)
        
        
        ## 85%
        arr = []
        for i in time:
            if i != ':' and i not in arr:
                arr.append(i)
        arr.sort()
        # print(arr)
        if len(arr) == 1:
            ans = arr[0] + arr[0] + ":" + arr[0] + arr[0]
        elif time[4] != arr[-1]:
            ans = time[:4] + arr[arr.index(time[4])+1]
        elif time[3] != arr[-1] and arr[arr.index(time[3])+1] < '6':
            ans = time[:3] + arr[arr.index(time[3])+1] + arr[0]
        elif time[0] in ['0', '1'] and time[1] != arr[-1]:
            ans = time[0] + arr[arr.index(time[1])+1] + ":" + arr[0] + arr[0]
        elif time[0] == '2' and arr[arr.index(time[1])+1] < '4':
            ans = time[0] + arr[arr.index(time[1])+1] + ":" + arr[0] + arr[0]
        else:
            ans = arr[0] + arr[0] + ":" + arr[0] + arr[0]
            
        return ans