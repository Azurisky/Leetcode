class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        dict_s1 = {}
        dict_s2 = {}
        for char in s1:
            dict_s1[char] = dict_s1.get(char,0) + 1
            
        for index,char in enumerate(s2):
            dict_s2[char] = dict_s2.get(char,0) + 1
            
            if (index >= len_s1):
                dict_s2[s2[index-len_s1]] -= 1
                if (dict_s2[s2[index-len_s1]] == 0):
                    dict_s2.pop(s2[index-len_s1])
            if (dict_s1 == dict_s2):
                return True
            # print(dict_s2)
            
        return False
        

            