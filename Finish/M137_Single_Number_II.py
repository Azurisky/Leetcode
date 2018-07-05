class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## bitwise
        a, b = 0, 0
        for n in nums:
            a, b = ~a & n | a & ~(b & n), (a & n) ^ b
        return a
            
        ## 
        N = 3
        K = 1
        Count = [0 for i in range(N)]
        NextCount = list(Count)
        Count[0] = ~0
        for n in nums:
            for i in range(N):
                # bits in n move from Count[i-1] to Count[i] if set in Count[i-1]
                # bit in n are cleared in Count[i] if in Count[i]
                NextCount[i] = (Count[i] & ~n) | (Count[i-1] & n)
            for i in range(N):
                Count[i] = NextCount[i]
        return NextCount[K]