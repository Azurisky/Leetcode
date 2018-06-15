class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        ## 100%
        ans = []
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                ans.append(s[:i] + '--' + s[i+2:])
        return ans