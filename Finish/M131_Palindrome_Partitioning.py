class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        
        def dfs(s, path):
            if not s:
                ans.append(path)
            
            for i in range(1, len(s)+1):
                if isPal(s[:i]):
                    dfs(s[i:], path + [s[:i]])
                    
        def isPal(s):
            return s == s[::-1]
        
        dfs(s, [])
        return ans