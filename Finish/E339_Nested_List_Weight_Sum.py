class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def sumList(nowList, depth):
            ans = 0
            for i in nowList:
                if i.isInteger():
                    ans += depth*i.getInteger()
                else:
                    ans += sumList(i.getList(), depth+1)
            return ans
        return sumList(nestedList, 1)