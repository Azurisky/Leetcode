class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        l = len(citations)
        
        ans = [0 for i in range(l+1)]
        for i in citations:
            if i >= l:
                ans[l] += 1
            else:
                ans[i] += 1
        
        count = 0
        i = l
        while i >= 0:
            count += ans[i]
            print(i, count)
            if count >= i:
                return i+1
            i -= 1
        return 0
        
        
        
        