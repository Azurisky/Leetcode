class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l = len(S)
        ans = [l] * (l)
        for i in range(l):
            if S[i] == C:
                ans[i] = 0
        for i in range(1, l):
            ans[i] = min(ans[i], ans[i-1]+1)
        
        for i in range(l-2, -1, -1):
            ans[i] = min(ans[i], ans[i+1]+1)
        
        return ans