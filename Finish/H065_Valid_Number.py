class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: 
            return False
        # strip the heading and tailing spaces of the string
        s = s.strip() 
        i = 0
        res = signs = eE = dot = False
        while i < len(s):
            if s[i].isdigit():
                i += 1
                res = signs = True
            elif s[i]=='.' and not dot:
                i += 1
                dot = signs = True
            elif (s[i]=='e' or s[i]=='E') and (not eE) and res:
                i += 1
                res = signs = False
                dot = eE = True
            elif (s[i]=='+' or s[i]=='-') and not res and not signs:
                i += 1
                signs = True
            else:
                return False
        
        if res:
            return True
        
        return False