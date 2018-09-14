class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        ## O(n), detect -1 in the beginning
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1
        position = 0
        balance = 0 # current tank balance
        for i in range(len(gas)):
            balance += gas[i] - cost[i] # update balance
            if balance < 0: # balance drops to negative, reset the start position
                balance = 0
                position = i+1
        return position
        
        
        ## TLE O(n^2)
        l = len(gas)
          
        for i in range(l):
            gas[i] = gas[i] - cost[i]
        gas.extend(gas)
        
        tmp = 0
        ans = 0
        for i, v in enumerate(gas):
            if i > l:
                break
            index = 0
            while tmp >= 0:
                # print(i, index)
                if index == l:
                    return i
                tmp += gas[i+index]
                index += 1
                if tmp < 0:
                    tmp = 0
                    index = 0
                    break
            
        return -1  