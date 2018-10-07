class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        removed = 0
        results = [s]
        count = {"(": 0, ")": 0}
        for i, c in enumerate(s):
            if c == ")" and count["("] == count[")"]:
                new_results = []
                while results:
                    result = results.pop()
                    for j in range(i - removed + 1):
                        if result[j] == ")":
                            if result[:j] + result[j + 1:] not in new_results:
                                new_results.append(result[:j] + result[j + 1:])
                results = new_results
                removed += 1
            else:
                if c in count:
                    count[c] += 1

        count = {"(": 0, ")": 0}
        i = len(s)
        ll = len(s) - removed
        for ii in range(ll - 1, -1, -1):
            i -= 1
            c = s[i]
            if c == "(" and count["("] == count[")"]:
                new_results = []
                while results:
                    result = results.pop()
                    for j in range(ii, ll):
                        if result[j] == "(":
                            if result[:j] + result[j + 1:] not in new_results:
                                new_results.append(result[:j] + result[j + 1:])
                results = new_results
                ll -= 1
            else:
                if c in count:
                    count[c] += 1
        print(results)
        return results
        
        
        ## dfs
        def dfs(s):
            mi = calc(s)
            if mi == 0:
                return [s]
            ans = []
            for x in range(len(s)):
                if s[x] in ('(', ')'):
                    ns = s[:x] + s[x+1:]
                    if ns not in visited and calc(ns) < mi:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans    
        def calc(s):
            a = b = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        visited = set([s])    
        return dfs(s)
#         stack = []
#         ans = ""
#         for i in s:
#             if i == '(':
#                 stack.append('(')
#             elif i == ')':
#                 if stack:
                    
#             else:
                