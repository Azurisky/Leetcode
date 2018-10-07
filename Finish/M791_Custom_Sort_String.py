class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        tmp = [[-1, 0] for i in range(26)]
        dic = {}
        
        for i, v in enumerate(S):
            tmp[ord(v) - ord('a')][0] = i
            dic[i] = v
        ans = ""
        
        for i, v in enumerate(T):
            if tmp[ord(v) - ord('a')][0] == -1:
                ans += v
            else:
                tmp[ord(v) - ord('a')][1] += 1
        for i in range(len(S)):
            ch = dic[i]
            ans += ch * tmp[ord(ch)-ord('a')][1]
        return ans
            