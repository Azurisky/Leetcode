class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        l = [1, 5, 10, 50, 100, 500, 1000]
        c = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        
        def findClose(l, num):
            if num == 4:
                return l[0]+l[1]
            elif num == 9:
                return l[0]+l[2]
            tmp = ""
            if num >= 5:
                tmp += l[1]
                num -= 5
            while num > 0:
                tmp += l[0]
                num -= 1
            return tmp
        
        count = 0
        scale = 10
        ans = ""
        while num:
            tmp = num%10
            ans = findClose(c[count:count+3], tmp) + ans
            num = num//10
            count += 2
        
        return ans