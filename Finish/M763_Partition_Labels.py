class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return [0]
        dic ={}
        l = len(S)
        for i in range(l):
            if S[i] in dic:
                dic[S[i]][1] = i
            else:
                dic[S[i]] = [i, i]
                
        ans = []
        pointer = 0
        tmpL, tmpR = dic[S[0]]
        
        while tmpR < l and pointer < l:
            tmpR = max(dic[S[pointer]][1], tmpR)
            if tmpR == pointer:
                ans.append(tmpR - tmpL + 1)
                if pointer+1 < l:   
                    tmpL = dic[S[pointer+1]][0]
            pointer += 1
        return ans
                
        
            