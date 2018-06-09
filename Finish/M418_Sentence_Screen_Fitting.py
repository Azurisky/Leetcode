class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """

        ## TLE
        count = 0
        col = 0
        row = 0
        while row < rows:
            for i in sentence:
                if col+len(i) <= cols:
                    col += len(i)+1
                else:
                    row += 1
                    if row == rows:
                        # print("minus")
                        count -= 1
                        break
                    else:
                        col = len(i)+1
            # print(row, col)
            count += 1
        return count

        ## Pass 
        ## https://leetcode.com/problems/sentence-screen-fitting/discuss/90869/Python-with-explanation
        s = ' '.join(sentence) + ' '
        start = 0
        for i in range(rows):
            start += cols - 1
            if s[start % len(s)] == ' ':
                start += 1
            elif s[(start + 1) % len(s)] == ' ':
                start += 2
            else:
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start // len(s)
