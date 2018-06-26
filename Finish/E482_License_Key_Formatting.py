class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        tmp = ''.join(S.split('-'))
        
        l = len(tmp)
        start = l%K
        ans = []
        if start != 0:
            ans.append(tmp[:l%K])
            
        while start < l:
            ans.append(tmp[start:start+K])
            start += K
        
        return '-'.join(ans).upper()
        
        
        
        
        