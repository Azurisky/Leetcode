class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
#         l = [0 for i in range(26)]
#         for i, v in enumerate(s):
#             print(l)
#             count = 0
#             index = ord(v) - ord('a')
#             if l[index] == 0:
#                 l[index] = i + 1
#             else:
#                 tmp = l[index]
#                 for j in range(index):
#                     if l[j] > tmp:
#                         count += 1
#             print(count, index)
#             if count == index:
#                  l[index] = i + 1
#         print(l)
#         ans = ""
#         for i in range(1, len(s)+1):
#             if i in l:
#                 ans += chr(l.index(i)+ord('a'))
#         return ans
        
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result