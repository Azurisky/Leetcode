class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if not n:
            return []
        ans = []
        def gen(l, r, count, s):
            if not l and not r:
                ans.append(s)
            elif not l:
                for i in range(r):
                    s += ')'
                ans.append(s)
            elif count > 0:
                gen(l-1, r, count+1, s + '(')
                gen(l, r-1, count-1, s + ')')
            else:
                gen(l-1, r, count+1, s + '(')
        
        gen(n-1, n, 1, '(')
        return ans
            