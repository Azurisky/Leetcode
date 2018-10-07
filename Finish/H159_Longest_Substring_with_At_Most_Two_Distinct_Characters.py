class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left, longest = 0, 0
        dic = {}
        max_d = 2
        
        for index, char in enumerate(s):
            dic[char] = index
            index_to_remove = float('inf')
            if len(dic) == max_d + 1:
                for key in dic:
                    if dic[key] < index_to_remove:
                        index_to_remove = dic[key]
                dic.pop(s[index_to_remove], None)
                left = index_to_remove + 1
            longest = max(longest, index - left + 1)
        return longest