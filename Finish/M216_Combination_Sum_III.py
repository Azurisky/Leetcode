class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ans = []
        def find(k, n, path, l):
            if n < 0 or k < 0:
                return
            elif k == 0 and n == 0:
                ans.append(path)
            for i, v in enumerate(l):
                find(k-1, n-v, path + [v], l[i+1:])
            
        find(k, n, [], l)
        return ans