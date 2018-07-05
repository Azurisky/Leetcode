class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Store the latest show up place
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                start = max(start, dic[ch]+1)
                res = max(res, i-start+1)
            else:
                res = max(res, i-start+1)
            dic[ch] = i
        return res

        ## TLE 
        ans = 0
        # if len(s) == 1:
        #     return 1
        for i in range(len(s)):
            tmp = []
            for j in range(i, len(s)):
                if s[j] not in tmp:
                    tmp.append(s[j])
                else:
                    break
            # print(tmp)
            ans = max(len(tmp), ans)
        
        return ans
                