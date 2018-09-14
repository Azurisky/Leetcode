class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        ## Pass
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                a, b = num[:i], num[i:j]
                if b != str(int(b)) or a != str(int(a)):
                    continue
                while j < n:
                    c = str(int(a) + int(b))
                    if c != num[j:j+len(c)]:
                        break
                    j += len(c)
                    a, b = b, c
                if j == n:
                    return True
        return False
        
        
        ## Can't handle too big number
        def dfs(first, rest):
            # print('new---')
            # print(first, rest)
            # print('---')
            if rest[0] == '0':
                return False
            l = len(rest)
            print(l)
            if l == len(str(first)):
                print('ya')
                return True
            for i in range(l//2):
                
                tmp = first + int(rest[:i+1])
                tmp_l = len(str(tmp))
                print('tmp---')
                print(str(tmp), rest[i+1:i+tmp_l+1], l)
                print('---')
                if str(tmp)== rest[i+1:i+tmp_l+1]:
                    return dfs(int(rest[:i+1]), rest[i+1:])
                
            return False
                
        for i in range(len(num)//2):
            s = str(num[:i+1])
            if dfs(int(s), num[i+1:]):
                return True
        return False
        