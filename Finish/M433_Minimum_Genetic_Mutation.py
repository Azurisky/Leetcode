class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        
        visit = []
        queue = [start]
        ans = 0
        tmp = []
        while queue:
            cur = queue.pop()
            visit.append(cur)
            for i in bank:
                count = 0
                for j in range(len(i)):
                    if cur[j] != i[j]:
                        count += 1
                    if count > 1:
                        break
                if count == 1 and i not in visit and i not in tmp:
                    if i == end:
                        return ans+1
                    else:
                        tmp.append(i)
            # print(tmp)
            if not queue:
                queue, tmp = tmp, []
                ans += 1
        
        return -1
                    