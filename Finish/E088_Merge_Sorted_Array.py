class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        index = m+n-1
        n -= 1
        m -= 1
        while index >= 0:
            # print(nums1)
            if n == -1:
                break
            if m == -1:
                nums1[:n+1] = nums2[:n+1]
                break
            if nums2[n] > nums1[m]:
                nums1[index] = nums2[n]
                n -= 1
            else:
                nums1[index] = nums1[m]
                m -= 1
            index -= 1
    