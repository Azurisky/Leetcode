class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # 95% Use map
        dic = {}
        ans = []
        c = 0
        for i in strings:
            tmp = i
            if i[0] != 'a':
                new = []
                shift = ord(i[0]) - ord('a')
                for s in i:
                    t = ord(s)-shift
                    if t > ord('z'):
                        t -= 26
                    elif t < ord('a'):
                        t += 26
                    new.append(chr(t))
                new_s = "".join(new)
                tmp = new_s
            if tmp not in dic:
                dic[tmp] = c
                ans.append([i])
                c += 1
            else:
                ans[dic[tmp]].append(i)
        # print(dic)
        return ans

        ## 37%
        dic = []
        ans = []
        for i in strings:
            tmp = i
            if i[0] != 'a':
                new = []
                shift = ord(i[0]) - ord('a')
                for s in i:
                    t = ord(s)-shift
                    if t > ord('z'):
                        t -= 26
                    elif t < ord('a'):
                        t += 26
                    new.append(chr(t))
                new_s = "".join(new)
                tmp = new_s
            if tmp not in dic:
                dic.append(tmp)
                ans.append([i])
            else:
                index = dic.index(tmp)
                ans[index].append(i)
        # print(dic)
        return ans