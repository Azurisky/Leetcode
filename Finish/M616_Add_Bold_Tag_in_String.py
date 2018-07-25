class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        ## 100%
        status = [False]*len(s)
        final = ""
        for word in dict:
            start = s.find(word)
            last = len(word)
            while start != -1:
                for i in range(start, last+start):
                    status[i] = True
                start = s.find(word,start+1)
        i = 0
        i = 0
        while i < len(s):
            if status[i]:
                final += "<b>"
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1
                final += "</b>"
            else:
                final += s[i]
                i += 1
        return final
        

        ## 70%
        group = {}
        l = []
        for i in dict:
            tmp = len(i)
            group[tmp] = group.get(tmp, [])
            group[tmp].append(i)
            if tmp not in l:
                l.append(tmp)
        l.sort()
        ans = ""
        start, end = len(s), 0
        flag = 0
        for i, v in enumerate(s):
            for j in l[::-1]:
                if s[i:i+j] in group[j]:
                    start = min(i, start)
                    end = max(end, i+j)
                    flag = 1
                    break
            if i == end and flag:
                ans += '<b>' + s[start:end] + '</b>'
                start = len(s)
                end = 0
                flag = 0
            if not flag:
                ans += v
        if flag:
            ans += '<b>' + s[start:end] + '</b>'
        return ans
        