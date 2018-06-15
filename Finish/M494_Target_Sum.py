class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        ## DP & math 98%
        if sum(nums)<S:  
            return 0  
        if (S+sum(nums))%2==1:  
            return 0  
        target = (S+sum(nums))//2  
        dp = [0]*(target+1)  
        dp[0] = 1  
        for n in nums:  
            i = target  
            while(i>=n):  
                dp[i] = dp[i] + dp[i-n]  
                i = i-1  
        return dp[target] 

        ## 32.85% 
        if sum(nums)<S:  
            return 0  
        l = len(nums)
        visit = [{} for i in range(l+1)]
        ans = 0
        
        if not nums:
            return 0
        queue = [[nums[0], 1], [-1*nums[0], 1]]
        visit[0][nums[0]] = 1
        visit[0][-1*nums[0]] = 1
        tmp = []
        i = 0

        while queue:
            p = queue.pop(0)
            v = p[0]
            c = p[1]
            
            if i+1 < len(nums):
                v_p = v + nums[i+1]
                v_m = v - nums[i+1]
                if v_p not in visit[i+1]:
                    visit[i+1][v_p] = c
                else:
                    visit[i+1][v_p] += c
                if v_m not in visit[i+1]:
                    visit[i+1][v_m] = c
                else:
                    visit[i+1][v_m] += c
            if not queue:
                for item in visit[i+1]:
                    tmp.append([item, visit[i+1][item]])
                # print(tmp)
                queue, tmp = tmp, []
                i += 1
        # print(visit)
        
        if S in visit[i-1]:
            return visit[i-1][S]
        else:
            return 0