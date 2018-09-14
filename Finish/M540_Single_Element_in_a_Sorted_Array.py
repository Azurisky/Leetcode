class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        l = len(nums)
        head = 0
        tail = l - 1
        
        while tail >= head:
            if tail == head:
                return nums[head]
            # print(head, tail)
            mid = (head + tail)//2
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    head = mid + 2
                elif nums[mid] == nums[mid-1]:
                    tail = mid - 2
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid+1]:
                    tail = mid - 1
                elif nums[mid] == nums[mid-1]:
                    head = mid + 1
                else:
                    return nums[mid]
        