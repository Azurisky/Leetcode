class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}
        
        for i in nums1:
            dic[i] = dic.get(i, 0)
            dic[i] += 1
        
        for j in nums2:
            if j in dic and dic[j] > 0:
                res.append(j)
                dic[j] -= 1
        
        return res