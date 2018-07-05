class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        dict={}
        longest=0
        fileList=input.split("\n")
        for i in fileList:
            if "." not in i:  # folder
                key = i.count("\t") # Level of folder
                value = len(i.replace("\t","")) # real length
                dict[key]=value
            else: # file
                key=i.count("\t")
                #　length of file
                length = sum([dict[j] for j in dict.keys() if j<key]) + len(i)
                longest=max(longest,length)
        return longest