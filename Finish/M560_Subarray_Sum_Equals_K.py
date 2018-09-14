class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        ## Special
        dic = {0:1}
        s = 0
        ans = 0
        for i in nums:
            s += i
            ans += dic.get(s-k, 0)
            dic[s] = dic.get(s, 0) + 1
        return ans
                