class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = {}
        for i in t:
            count[i] = count.get(i, 0)
            count[i] += 1
        missing = len(t)
        i = 0
        mi = len(s)
        ans = ''
        for j, v in enumerate(s):
            if v not in count:
                continue
            if count[v] > 0:
                missing -= 1
            # missing -= count[v] > 0
            count[v] -= 1
            if not missing:
                while i < j:
                    if s[i] in count and count[s[i]] < 0:
                        count[s[i]] += 1
                        i += 1
                    elif s[i] in count and count[s[i]] == 0:
                        break
                    else:
                        i += 1
                if j-i < mi:
                    mi = j-i
                    ans = s[i:j+1]
        return ans
        
        ## Can't handle duplicate item in T
        l = []
        dic = {}
        count = {}
        leng = len(s)
        ans = ""
        for i, v in enumerate(s):
            if v in t:
                if v in dic:
                    index = l.index(dic[v])
                    l = l[:index] + l[index+1:]
                dic[v] = i
                l.append(i)

                if len(l) == len(t):
                    mi = min(l)
                    ma = max(l)
                    if ma - mi < leng:
                        leng = ma - mi
                        ans = s[mi:ma+1]
        return ans
                
            
            