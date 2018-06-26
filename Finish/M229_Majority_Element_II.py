class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## Boyer-Moore Algorithm, http://goo.gl/64Nams
        elem1, elem2, count1, count2 = 0,0,0,0
        for i in nums:
            if count1 == 0 and i != elem2:
                elem1 = i
            if i == elem1:
                count1 += 1
            elif i != elem1:
                if count2 == 0:
                    elem2 = i
                if i == elem2:
                    count2 +=1
                elif i != elem2:
                    count1 -=1
                    count2 -=1
        output = []
        if count1 > 0 and nums.count(elem1) > len(nums) // 3:
            output.append(elem1)
        if count2 > 0 and nums.count(elem2) > len(nums) // 3:
            output.append(elem2)
        return output
        

        ## 49% and not O(1) space
        if not nums:
            return []
        l = len(nums)
        dic = {}
        ans = []
        for i in nums:
            dic[i] = dic.get(i, 0)
            dic[i] += 1
        print(dic)
        for i in dic:
            if dic[i] > l/3 :
                ans.append(i)
        return ans
                