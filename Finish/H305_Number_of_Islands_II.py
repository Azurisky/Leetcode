class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ## Union Find
        group = {}
        belong = {}
        ans = []
        def getParent(num):
            if num != belong[num]:
                belong[num] = getParent(belong[num])
            return belong[num] 

        for (i, j) in positions:
            num = i*n + j
            belong[num] = num
            if num%n == 0:
                s = [num+1, num-n, num+n]
            elif num%n == n-1:
                s = [num-1, num-n, num+n]
            else:
                s = [num-1, num+1, num-n, num+n]
            for elem in s:
                if elem in belong:
                    p = getParent(elem)
                    belong[p] = num
                    group.pop(p, None)
            group[num] = num
            ans.append(len(group))
        return ans

        
        
        ## TLE
        belong = {}
        group = {}
        
        def findGroup(num):
            flag = 0
            relate = []
            if num%n == 0:
                s = [num+1, num-n, num+n]
            elif num%n == n-1:
                s = [num-1, num-n, num+n]
            else:
                s = [num-1, num+1, num-n, num+n]
            for item in s:
                if item in belong and belong[item] not in relate:
                    relate.append(belong[item])
            # print('relate: {}'.format(relate))
            
            group[num] = [num]
            # print('group: {}'.format(group))
            if relate:
                relate.append(num)
                mi = min(relate)
                for item in relate:
                    if item != mi and item in group:
                        group[mi] += group[item]
                        group.pop(item, None)
                for elem in group[mi]:
                    belong[elem] = mi
            else:
                belong[num] = num
                
            # print(belong)
            # print(group)
            return len(group)
                    
                    
        ans = []
        for (i, j) in positions:
            # print(i*m + j)
            ans.append(findGroup(i*n + j))
            # print('------')
        
        return ans