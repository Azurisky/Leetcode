class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ## https://leetcode.com/problems/intersection-of-two-arrays/discuss/82006/Four-Python-solutions-with-simple-explanation
        res = []
        dic = {}
        
        for i in nums1:
            dic[i] = dic.get(i, 0)
            dic[i] += 1
        
        for j in nums2:
            if j in dic and dic[j] > 0:
                res.append(j)
                dic[j] = 0
        
        return res