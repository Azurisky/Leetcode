class Solution:
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {}
        def recurse(state):
            if state not in lookup:
                canWin = False
                for i in range(len(state) - 1):
                    if state[i:i + 2] == "++":
                        canWin |= not recurse(state[:i] + "--" + state[i + 2:])
                lookup[state] = canWin
            return lookup[state]
        return recurse(s)
        