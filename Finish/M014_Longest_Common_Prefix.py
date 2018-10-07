class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        mi = float('inf')
        shortest = ''
        for i in strs:
            if len(i) < mi:
                mi = len(i)
                shortest = i
                
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
                
        return shortest 