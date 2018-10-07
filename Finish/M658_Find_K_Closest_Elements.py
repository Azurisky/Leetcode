class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        l = 0
        r = n-1
        flag = 0
        
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == x:
                flag = 1
                break
            elif arr[mid] > x:
                r = mid-1
            else:
                l = mid+1
        pos = 0
        if flag:
            pos = mid
        else:
            pos = l
        
        right = left = pos
        while right - left < k:
            if left == 0: 
                return arr[:k]
            if right == len(arr): 
                return arr[-k:]
            if x - arr[left - 1] <= arr[right] - x: 
                left -= 1
            else:
                right += 1
        return arr[left:right]
            
        