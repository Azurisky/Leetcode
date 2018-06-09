class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack = []
        for i in s:
            if i in ["{", "(", "["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                tmp = stack.pop()
                if i == "}" and tmp != "{" or i == "]" and tmp != "[" or i == ")" and tmp != "(":
                    return False
        if stack:
            return False
        return True