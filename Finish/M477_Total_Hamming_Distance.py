class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## Bitwise
        l = [[0, 0] for i in range(32)] 
        # print(l)
        for i in nums:
            for j in range(32):
                l[j][i%2] += 1
                i /= 2
        ans = 0
        for i, j in l:
            ans += i*j
        return ans
                
        
        ## TLE
        l = len(nums)
        List = []
        
        for i in range(l):
            for j in range(i, l):
                List.append([nums[i], nums[j]])
        ans = 0
        for i, j in List:
            tmp = i ^ j
            count = 0
            while tmp:
                tmp &= (tmp-1)
                count += 1
            ans += count
        
        return ans
            