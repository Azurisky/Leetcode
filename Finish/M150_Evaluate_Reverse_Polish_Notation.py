class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def cal(f, op, s):
            if op == '+':
                return f+s
            elif op == '-':
                return f-s
            elif op == '*':
                return f*s
            else:
                return int(f/s)
            
        stack = []
        for i in tokens:
            # print(stack)
            if i in ['+', '-', '*', '/']:
                first = stack.pop()
                second = stack.pop()
                stack.append(cal(second, i, first))
            else:
                stack.append(int(i))
        return stack[-1]