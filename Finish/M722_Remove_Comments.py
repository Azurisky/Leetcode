class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        
        result, parseLine, flag, fInd = [], [], False, -1
        for line in source:
            for i,c in enumerate(line):
                if not flag:
                    if c == '/' and i != len(line)-1 and line[i+1] in ('*', '/'): # comment start token
                        if line[i+1] == '/': # if line comment, skip to end
                            break
                        flag, fInd = True, i+1 # activate flag and record position
                    else:
                        parseLine.append(c) # valid char
                elif c == '/': # potential block end
                    prev = max(0, i-1)
                    flag = (fInd == prev) or (line[prev] != '*')
            if not flag: # a parsed line can only be complete at the end of a line
                if parseLine: # only append if line isn't empty
                    result.append(''.join(parseLine))
                    parseLine = []
            fInd = -1 # reset block comment start as the current line is done.
        return result