class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ## Traverse left and right
        traverse_map = {}
        mx = 0
        for item in nums:
            if item not in traverse_map:
                l, r = item, item
                if l - 1 in traverse_map:
                    l, _ = traverse_map[l - 1]
                if r + 1 in traverse_map:
                    _, r = traverse_map[r + 1]
                traverse_map[item] = [l,r]
                traverse_map[l] = [l, r]
                traverse_map[r] = [l, r]
                if r - l + 1 > mx:
                    mx = r - l + 1
        print(traverse_map)
        return(mx)
        
        ## Have a set first, faster
        max_count = 0
        s = {}
        for i in nums:
            s[i] = i
        # print(s)
        for i in nums:
            cnt = 1
            tmp = i-1
            while tmp in s:
                cnt += 1
                s.pop(tmp, None)
                tmp -= 1
                
            tmp = i+1
            while tmp in s:
                cnt += 1
                s.pop(tmp, None)
                tmp += 1
            
            max_count = max(max_count, cnt)
        # print(s)
        return max_count
                