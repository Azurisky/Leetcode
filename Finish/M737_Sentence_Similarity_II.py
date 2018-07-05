class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        ## 95%, only store the parent 
        if len(words1) != len(words2):
            return False
        
        parent_dict = {w:w for p in pairs for w in p}
        
        def find(w):
            while parent_dict[w] != w:
                w = parent_dict[w]
            return w
        
        for w1, w2 in pairs:
            r1, r2 = find(w1), find(w2)
            if r1 != r2:
                parent_dict[r1] = r2
        
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            if w1 not in parent_dict or w2 not in parent_dict or find(w1) != find(w2):
                return False
            
        return True


        ## 25%
        dic = {}
        for i in pairs:
            if i[0] in dic and i[1] in dic:
                dic[i[0]].append(i[1])
                for k in dic[i[1]]:
                    if k not in dic[i[0]]:
                        dic[i[0]].append(k)
                for k in dic[i[0]]:
                    dic[k] = dic[i[0]] 
            elif i[0] in dic:
                dic[i[0]].append(i[1])
                for k in dic[i[0]]:
                    dic[k] = dic[i[0]] 
                # dic[i[1]] = dic[i[0]]
            elif i[1] in dic:
                dic[i[1]].append(i[0])
                for k in dic[i[1]]:
                    dic[k] = dic[i[1]] 
                # dic[i[0]] = dic[i[1]]
            else:
                dic[i[0]] = [i[0]]
                dic[i[0]].append(i[1])
                dic[i[1]] = [i[1]]
                dic[i[1]].append(i[0])
        
        if len(words1) != len(words2):
            return False
        # print(dic)
        for i, v in enumerate(words1):
            print(v)
            dic[v] = dic.get(v, [])
            if words2[i] != v and words2[i] not in dic[v]:
                return False
        return True