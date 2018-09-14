class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ## dfs
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        digits = digits.strip('1')
        ans = []
        l = len(digits)
        if not digits:
            return []
        def dfs(digit, path):
            if not digit and len(path) == l:
                ans.append("".join(path))
            for i, v in enumerate(digit):
                for c in mapping[v]:
                    dfs(digit[i+1:], path + [c])
        
        dfs(digits, [])
    
        return ans
        

        ## iteration
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        ans = ['']
        for i in digits:
            tmp = []
            for j in ans:
                for k in mapping[i]:
                    tmp.append(j+k)
            ans = tmp
        
        return ans
            
                     