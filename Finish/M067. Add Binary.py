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
        result = ''
        index = 0
        
        carry = '0'
        while index < max(len(a), len(b)) or carry == '1':
            num_a = a[-1 - index] if index < len(a) else '0'
            num_b = b[-1 - index] if index < len(b) else '0'
            
            val = int(num_a) + int(num_b) + int(carry)
            result = str(val % 2) + result
            
            carry = '1' if val > 1 else '0'
            index += 1

        return result
        