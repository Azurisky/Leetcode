class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ## https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step

        ## O(m*n)
        sub = []
        for val in nums:
            pos , sub_len = 0, len(sub)
            while(pos <= sub_len):    # update the element to the correct position of the sub.
                if pos == sub_len:
                    sub.append(val)
                    break
                elif val <= sub[pos]:
                    sub[pos] = val
                    break
                else:
                    pos += 1
        return len(sub)

        ## O(nlogn), Best
        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)

        ## dp
        if not nums:
            return 0
        
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)