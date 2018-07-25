class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ## DP but optimize, O(n ** 2)
        n = len(s)
        res = list(range(-1, n))
        for i in range(n):
            for [l, r] in [[i, i], [i, i + 1]]:
                while l >= 0 and r < n and s[l] == s[r]:
                    res[r + 1] = min(res[r + 1], res[l] + 1)
                    l -= 1
                    r += 1
        return res[n]
        
        ## DP, O(n ** 3)
        cut = [x for x in range(-1,len(s))]
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j+1] = min(cut[j+1],cut[i]+1)
        return cut[-1]
        
        ## TLE
        ans = []
        def dfs(s, cut):
            if not s:
                ans.append(cut)
            for i in range(len(s), 0, -1):
                if isPal(s[:i]):
                    dfs(s[i:], cut+1)
                    
        def isPal(s):
            return s == s[::-1]
    
        dfs(s, -1)
        return min(ans) 

        