class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        def dfs(end, index, path, ans):
            while index ** 2 <= end:
                if end % index == 0:
                    ans.append(path + [index, end//index])
                    dfs(end//index, index, path+[index], ans)
                index += 1
            return ans
        
        return dfs(n, 2, [], [])