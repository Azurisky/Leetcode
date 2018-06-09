class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # https://fizzbuzzed.com/top-interview-questions-2/#solutioncode
        x = len(nums1)
        y = len(nums2)
        total = x + y
        
        if total % 2 == 0:
            first = self.getKth(nums1, nums2, total // 2 - 1)
            second = self.getKth(nums1, nums2, total // 2)
            return (first + second) / 2
        else:
            return self.getKth(nums1, nums2, total // 2)  
        
    
    def findMedian(self, nums):
        if len(nums)%2 == 1:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
        
    def getKth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k]
        if len(nums2) == 0:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])
        
        mid1 = min(len(nums1), (k + 1) // 2)
        mid2 = min(len(nums2), (k + 1) // 2)
        
        a = nums1[mid1 - 1]
        b = nums2[mid2 - 1]
        
        if a > b:
            return self.getKth(nums1, nums2[mid2:], k-mid2)
        return self.getKth(nums1[mid1:], nums2, k-mid1)
        
        
                