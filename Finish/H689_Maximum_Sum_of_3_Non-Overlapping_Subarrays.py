class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ksum = [sum(nums[:k])]
        for i in range(1,len(nums)-k+1):
            ksum += [ksum[-1]+nums[i+k-1]-nums[i-1]]
        
        left, right = [0]*len(nums), [0]*len(nums)
        maxsum, maxi = -sys.maxint, 0
        for i in range(0,len(nums)-k+1):
            if ksum[i]>maxsum:
                maxsum, maxi = ksum[i], i
            left[i] = maxi
            
        maxsum = -sys.maxint
        for i in range(len(nums)-k, -1, -1):
            if ksum[i]>=maxsum:
                maxsum, maxi = ksum[i], i
            right[i] = maxi
            
        maxsum, ret = -sys.maxint, []
        for i in range(k, len(nums)-2*k+1):
            newsum = ksum[i]+ksum[left[i-k]]+ksum[right[i+k]]
            if newsum > maxsum:
                maxsum = newsum
                ret = left[i-k], i, right[i+k]
        return ret