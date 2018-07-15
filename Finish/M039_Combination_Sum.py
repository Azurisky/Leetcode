class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ans = []
        def find(target, path, C):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return
            elif target > 0:
                for i, v in enumerate(C):
                    find(target - v, path + [v], C[i:])
        find(target, [], candidates)
        return ans
    
            