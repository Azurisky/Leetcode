class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Store the latest show up place
        l = len(s)
        start = 0
        end = 1
        ans = 0
        dic = {}
        if not s:
            return 0
        if len(s) == 1:
            return 1  
        dic[s[0]] = 0
        for i in range(1, l):
            if s[i] in s[start:i]:
                start = dic[s[i]]+1
            if len(s[start:i+1]) > ans:
                ans = len(s[start:i+1])
            dic[s[i]] = i
        return ans

        ## store the place as well
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                start = max(start, dic[ch]+1)
                res = max(res, i-start+1)
            else:
                res = max(res, i-start+1)
            dic[ch] = i
        return res

        ## 55%
        l = len(s)
        start = 0
        end = 1
        ans = 0
        if len(s) == 1:
            return 1    
        for i in range(1, l):
            if s[i] in s[start:i]:
                start += 1
                while s[i] in s[start:i]:
                    start += 1
            if len(s[start:i+1]) > ans:
                ans = len(s[start:i+1])
        return ans
                