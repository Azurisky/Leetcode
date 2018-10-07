class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        ans = [0 for i in range(len(num1)+len(num2))]
        pos = len(ans)-1
        
        for n1 in reversed(num1):
            tmpPos = pos
            for n2 in reversed(num2):
                tmp = int(n1) * int(n2)
                ans[tmpPos] += tmp
                ans[tmpPos-1] += ans[tmpPos] // 10
                ans[tmpPos] %= 10
                tmpPos -= 1
            pos -= 1
        print(ans)
        pt = 0
        while pt < len(ans)-1 and ans[pt] == 0:
            pt += 1

        return ''.join(map(str,ans[pt:]))
    
    
    
    