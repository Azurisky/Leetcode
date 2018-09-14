class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        exist = {}
        for i, v in enumerate(s):
            if v not in dic and t[i] not in exist:
                dic[v] = t[i]
                exist[t[i]] = 1
            elif v not in dic and t[i] in exist:
                return False
            else:
                if dic[v] != t[i]:
                    return False
        return True