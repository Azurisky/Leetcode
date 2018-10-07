    class Solution(object):
    # heap solution:
    # Build max heap: Time Complexity = O(n)
    # Take max element out: Time Comlexity = O(logn), do k times: = O(klogn)
    # Overall:
    # Time Complexity = O(n + klogn)
    # Space Complexity = O(n)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        return heapq.nlargest(k, nums)[-1]

    # Sort solution:
    # list inplace sort: Time Complexity = O(nlogn), Space Complexity = O(1)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if not nums:
            return None
        nums.sort()
        print(nums[::-1])
        return (nums[::-1][k-1])
        
    # Quick Select solution.
    # Time Complexity = O(n)
    # Space Complexity = O(logn)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """    v
        low = 0
        high = len(nums) - 1
        # Shuffle to avoid the worst case
        random.shuffle(nums)
        while low <= high:
            pIndex = self.partition(nums, low, high)
            if k < pIndex + 1:
                high = pIndex - 1
            elif k > pIndex + 1:
                low = pIndex + 1
            else:
                return nums[pIndex]

    def partition(self, nums, start, end):
        pIndex = start
        pivot = nums[end]
        for i in range(start, end):
            if nums[i] > pivot:
                nums[i], nums[pIndex] = nums[pIndex], nums[i]
                pIndex += 1
        nums[pIndex], nums[end] = nums[end], nums[pIndex]
        return pIndex