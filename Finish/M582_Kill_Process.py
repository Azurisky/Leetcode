class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        ## Pass Use dic as map to avoid loop 
        dic = {}
        for i in range(len(pid)):
            if ppid[i] not in dic:
                dic[ppid[i]] = [pid[i]]
            else:
                dic[ppid[i]].append(pid[i])
            
        queue = [kill]
        ans = []
        while queue:
            
            tmp = queue.pop(0)
            # print(tmp)
            ans.append(tmp)
            queue.extend(dic.get(tmp, []))
            print(queue)
            print(dic.get(tmp, []))
        return ans

        ## TLE
        queue = [kill]
        ans = []
        while queue:
            tmp = queue.pop()
            if tmp not in ans:
                ans.append(tmp)
                if tmp in ppid:
                    for i in range(len(ppid)):
                        if ppid[i] == tmp:
                            queue.append(pid[i])
        return ans

