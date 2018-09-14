class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## recursive
        def searchMin(head, tail, nums):
            print(head, tail)
            if head >= tail:
                return nums[head]
            mid = (head + tail) //2
            if nums[head] <= nums[mid] <= nums[tail]:
                return nums[head]
            elif nums[head] >= nums[mid] >= nums[tail]:
                return nums[tail]
            elif nums[head] < nums[mid]:
                return searchMin(mid+1, tail, nums)
            else:
                return searchMin(head, mid, nums)
        
        if not nums:
            return 0
        return searchMin(0, len(nums)-1, nums)
        
        ## iteration
        l = len(nums)
        head = 0
        tail = l-1
        while head < tail:
            mid = (head + tail) // 2 
            if nums[head] <= nums[mid] <= nums[tail]:
                return nums[head]
            elif nums[tail] <= nums[mid] <= nums[head]:
                return nums[tail]
            elif nums[mid] > nums[head]:
                head = mid + 1
            else:
                tail = mid
                
        return nums[head]
        
        
        