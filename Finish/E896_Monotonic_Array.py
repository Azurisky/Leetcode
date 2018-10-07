class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc = 0
        dec = 0
        index = 0
        if len(A) < 3:
            return True
        while index < len(A)-1:
            if A[index] == A[index+1]:
                index += 1
            elif A[index] > A[index+1]:
                if not inc and not dec:
                    dec = 1
                    index += 1
                elif dec != 1:
                    return False
                else:
                    index += 1
            else:
                if not inc and not dec:
                    inc = 1
                    index += 1
                elif inc != 1:
                    return False
                else:
                    index += 1
        return True