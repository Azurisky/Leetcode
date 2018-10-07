class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        case = ["", "Thousand", "Million", "Billion"]
        count = 0
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        ans = []
        def analyze(tmp):
            if tmp < 20:
                return to19[tmp-1:tmp]
            elif tmp < 100:
                return [tens[(tmp//10) - 2]] + analyze(tmp%10)
            else:
                return [to19[(tmp//100) - 1]] + ['Hundred'] + analyze(tmp%100)
                       
        while num > 0:
            if count:
                if analyze(num%1000):
                    ans = analyze(num%1000) + [case[count]] + ans
            else:
                ans = analyze(num%1000)
            num //= 1000
            count += 1
       
        return " ".join(ans)
        