class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Faster 
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        return left

        ## Myself
        nums = [float('-inf')] + nums
        nums.append(float('-inf'))
        head = 0
        tail = len(nums)-1
        
        while head < tail:
            
            mid = (head + tail)/2
            # print(head, tail, mid)
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid+1] > nums[mid] > nums[mid-1]:
                head = mid
            elif nums[mid+1] < nums[mid] < nums[mid-1]:
                tail = mid
            else:
                tail = mid
        
            