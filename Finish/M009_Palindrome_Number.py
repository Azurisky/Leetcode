class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        ## Reverse all number
        if x < 0:
            return False
        elif -1 < x <10:
            return True
        else:
            num = x
            reversedNum = 0
            while num != 0:
                reversedNum = reversedNum * 10 + num % 10;
                num = num // 10
            # reversedNumber = self.reverseNumList(x)
            if(reversedNum == x):
                return True
            else:
                return False
        
            
        ## Pass
        if x<0:
            return False
        count = 0
        tmp = x
        while tmp != 0:
            tmp //= 10
            count += 1

        if count%2 == 1:
            s = x % (10 ** (count//2))
            l = x // (10 ** ((count//2)+1))
        else:
            s = x % (10 ** (count//2))
            l = x // (10 ** (count//2))

        ans = 0
        while l != 0:
            ans *= 10
            ans += l % 10
            l //= 10
        
        if ans == s:
            return True
        else:
            return False
    
            