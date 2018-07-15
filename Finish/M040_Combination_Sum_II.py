class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        candidates.sort()
        result = []

        def backtracing(sub_candidate, rest, tmp):
            if rest == 0:
                result.append(tmp)
                return
            if rest < 0:
                return
            for i, v in enumerate(sub_candidate):
                if rest - v < 0:
                    break
                if i > 0 and v == sub_candidate[i-1]:
                    continue
                backtracing(sub_candidate[i+1:], rest - v, tmp + [v])
        
        backtracing(candidates, target, [])
        return result