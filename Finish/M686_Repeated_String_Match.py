class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i = 0
        l = len(A)
        
        while i < l:
            if A[i] == B[0]:
                s, e = i, i+len(B)
                
                if e%l == 0:
                    repeat = e//l 
                else:
                    repeat = e//l + 1
                tmp = A*repeat
                if tmp[s:e] == B:
                    return repeat
            i += 1
        return -1