class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, stack = 0, 0, 1, [1]
        for i in s+"+":
            if i.isdigit():
                num = 10*num + int(i)
            elif i in "+-":
                res += num * sign * stack[-1]
                if i == '+':
                    sign = 1  
                else:
                    sign = -1
                num = 0
            elif i == "(":
                stack.append(sign * stack[-1])
                sign = 1
            elif i == ")":
                res += num * sign * stack[-1]
                stack.pop()
                num = 0
            # print(i, sign, num, res)
        return res