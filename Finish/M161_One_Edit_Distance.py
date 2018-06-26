class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## 80%
        if s == t:
            return False
        if len(s) == len(t):
            encountered = False
            for i in range(len(s)):
                if s[i] != t[i] and encountered:
                    return False
                if s[i] != t[i]:
                    encountered = True
            return True
        if len(s) - len(t) > 1 or len(t) - len(s) > 1:
            return False
        i = 0
        j = 0
        missing = False
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if missing:
                    return False
                if len(s) < len(t):
                    j += 1
                else:
                    i += 1
                missing = True
        return True
    
        ## 25%
        if len(t) == len(s):
            print("==")
            if s == t:
                return False
            for i in range(len(s)):
                tmps = s[:i] + s[i+1:]
                tmpf = t[:i] + t[i+1:]
                if tmps == tmpf:
                    return True
        elif len(t) > len(s):
            s, t = t, s
        for i in range(len(s)):
                tmp = s[:i] + s[i+1:]
                if tmp == t:
                    return True
        return False