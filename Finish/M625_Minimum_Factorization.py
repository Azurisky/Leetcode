class Solution:
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        
        if a == 1:
            return 1
        count = 9
        dic = {}
        while count > 1:
            while a % count == 0:
                dic[count] = dic.get(count, 0)
                dic[count] += 1
                a = a// count
            count -= 1
        if a != 1:
            return 0
        
        print(dic)
        ans = ""
        for i in range(2, 10):
            if i in dic:
                ans += str(i) * dic[i]
    
        if int(ans) > 2**31:
            return 0
        else:
            return int(ans)
        
        