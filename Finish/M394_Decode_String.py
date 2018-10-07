class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = 0
        num = 0
        stack = []
        ans = ''
        tmp = ''
        while index < len(s):
            if s[index].isdigit():
                num = num*10 + int(s[index])
            elif s[index] == '[':
                stack.append([num, tmp])
                tmp = ''
                num = 0
            elif s[index] == ']':
                n, t = stack.pop()
                tmp = t + tmp * n
                if not stack:
                    ans = ans + tmp
                    tmp = ''
            else:
                tmp += s[index]
            index += 1
        if tmp:
            ans += tmp
        return ans
        