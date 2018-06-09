class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ## Use Sort to be faster
        index = 0
        hashTable = {}
        output = []
        for str in strs:
            hash = ''.join(sorted(str))
            if (hash in hashTable):
                output[hashTable[hash]].append(str)
            else:
                hashTable[hash] = index
                output.append([str])
                index += 1
        return output

        ## 29%
        construct = [[0]*26 for i in strs]
        # print(construct)
        for i, word in enumerate(strs):
            for j, v in enumerate(word):
                construct[i][ord(v)-ord("a")] += 1
        
        tmp = []
        # print(construct)
        for i in construct:
            t = "".join(str(i))
            tmp.append(t)
                
        # print(tmp)
        dic = {}
        for i in range(len(tmp)):
            if tmp[i] not in dic:
                dic[tmp[i]] = [strs[i]]
            else:
                dic[tmp[i]].append(strs[i])
        # print(dic)
        
        ans = []
        for i in dic:
            ans.append(dic[i])
        
        return ans