class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        dic = {}
        if len(words1) != len(words2):
            return False
            
        for [x, y] in pairs:
            dic[x] = dic.get(x, [])
            dic[x].append(y)
            dic[y] = dic.get(y, [])
            dic[y].append(x)
            
                
        for (x, y) in zip(words1, words2):
            if x == y:
                continue
            if x not in dic or y not in dic[x]:
                return False

        return True
        