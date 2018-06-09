class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        ans = [0, 1]
        while len(ans) <= num:
            tmp = []
            tmp.extend(ans)
            for i, v in enumerate(tmp):
                ans.append(v+1)
        return ans[:num+1]
        