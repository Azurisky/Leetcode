class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        head = 0
        tail = len(nums) - 1
        
        while head <= tail:
            mid = (head+tail)//2
            if nums[mid] == target:
                print(mid)
                s, e = mid, mid
                while s-1 >= 0 and nums[s-1] == target:
                    s -= 1
                while e+1 < len(nums) and nums[e+1] == target:
                    e += 1
                return [s, e]
            elif nums[mid] > target:
                tail = mid - 1
            else:
                head = mid + 1
        
        return [-1, -1]
            
        
        