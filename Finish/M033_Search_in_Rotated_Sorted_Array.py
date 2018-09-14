class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.binarySearch(nums, target, 0, len(nums)-1)

    def binarySearch(self, nums, target, start, end):
        if end < start:
            return -1
        mid = int((start+end)/2)
        if nums[mid] == target:
            return mid
        if nums[start] <= target < nums[mid]: # left side is sorted and has target
            return self.binarySearch(nums, target, start, mid-1)
        elif nums[mid] < target <= nums[end]: # right side is sorted and has target
            return self.binarySearch(nums, target, mid+1, end)  
        
        elif nums[start] > nums[mid]: # left side is pivoted
            return self.binarySearch(nums, target, start, mid-1)
        else: # right side is pivoted
            return self.binarySearch(nums, target, mid+1, end)