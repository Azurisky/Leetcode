class Solution:

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        ## Start from mid, 80%
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

        ## slow
        m = 0
        l = len(s)
        ans = s[0]
        for i in range(l):
            for j in range(l-1, i, -1):
                tmp = j-i
                if m > tmp:
                    break
                if tmp%2 == 1:
                    if s[i:i+tmp//2+1] == s[j:i+tmp//2:-1]:
                        # print(s[i:i+tmp//2+1], s[i+tmp//2+1:j+1:-1])
                        m = tmp
                        ans = s[i:j+1]
                else:
                    if s[i:i+tmp//2] == s[j:i+tmp//2:-1]:
                        # print(s[i:i+tmp//2+1], s[i+tmp//2+1:j+1:-1])
                        m = tmp
                        ans = s[i:j+1]
        return ans