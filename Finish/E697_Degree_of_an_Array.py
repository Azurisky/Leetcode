class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_map = {}
        deg = 0
        min_len = float('inf')
        for index, num in enumerate(nums):
            nums_map[num] = nums_map.get(num, [])
            nums_map[num].append(index)
            if len(nums_map[num]) == deg:
                min_len = min(min_len, nums_map[num][-1] - nums_map[num][0] + 1)
            elif len(nums_map[num]) > deg:
                deg = len(nums_map[num])
                min_len = nums_map[num][-1] - nums_map[num][0] + 1
        return min_len
        
        
        
        ## TLE
        dic = {}
        max = 0
        candidate = []
        for i in nums:
            dic[i] = dic.get(i, 0)
            dic[i] += 1
            if dic[i] >= max:
                max = dic[i]
        for i in nums:
            if dic[i] == max:
                candidate.append(i)
        ans = len(nums)
        
        for j in candidate:
            flag = 0
            for i, v in enumerate(nums):
                if v == j:
                    if not flag:
                        first = i
                        last = i
                        flag = 1
                    else:
                        last = i
            ans = min(ans, last-first+1)
            
        return ans
                    
                    
                    