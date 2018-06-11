class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        ## Use map to save time
        stack = [[s, 0]]
        visited = {}
        while stack:
            tmp, leng = stack.pop()
            if tmp in visited:
                continue
            visited[tmp] = 1
            # print(tmp, leng)
            for i in wordDict:
                l = len(i)
                if leng+l <= len(s) and tmp[:l] == i:
                    if leng+l == len(s):
                        return True
                    else:
                        stack.append([tmp[l:], leng+l])
        return False
        
        ## TLE
        stack = [[s, 0]]
        while stack:
            tmp, leng = stack.pop()
            # print(tmp, leng)
            for i in wordDict:
                l = len(i)
                if leng+l <= len(s) and tmp[:l] == i:
                    if leng+l == len(s):
                        return True
                    else:
                        stack.append([tmp[l:], leng+l])
        return False
    

                