class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        ## recusrive
        ans = ''
        if not a:
            return b
        if not b:   
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'

        ## iteration
        index = 0
        
        carry = '0'
        while index < max(len(a), len(b)) or carry == '1':
            if index < len(a):
                num_a = a[-1 - index] 
            else:
                num_a = '0'
            if index < len(b):
                num_b = b[-1 - index] 
            else:
                num_b = '0'
        
            val = int(num_a) + int(num_b) + int(carry)
            result = str(val % 2) + result
            if val > 1:
                carry = '1'
            else:
                carry = '0'
            index += 1

        return result
        