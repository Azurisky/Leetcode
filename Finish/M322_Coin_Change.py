class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # BFS
        if amount == 0:
            return 0
        queue = [[amount, 0]]
        visited = [False]*(amount+1)
        
        while queue:
            target, count = queue.pop(0)
            for i in coins:
                tmp = target - i
                c = count + 1
                if tmp > 0:
                    if not visited[tmp]:
                        queue.append([tmp, c])
                        visited[tmp] = True
                elif tmp == 0:
                    return c
        
        return -1 

        # DP
        res = [-1]*(amount+1)     
        res[0] = 0
        count = 0
        for i in range(len(res)):
            # print(i, res)
            if res[i] != -1:
                for c in coins:
                    if i+c > amount:
                        continue
                    else:
                        if res[i+c] != -1:
                            res[i+c] = min(res[i]+1, res[i+c])
                        else:
                            res[i+c] = res[i]+1
        return res[-1]
            
        