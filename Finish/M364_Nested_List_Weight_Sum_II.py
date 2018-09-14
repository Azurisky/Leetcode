# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        ## dfs
        def depth(nestedList):
            curr_depth = 1
            for x in nestedList:
                if x.isInteger() == False:
                    curr_depth = max(curr_depth, 1+depth(x.getList()))
            return curr_depth
        
        def dfs(nestedList, depth):
            ans = 0
            for i in nestedList:
                if i.isInteger():
                    ans += depth*i.getInteger()
                else:
                    ans += dfs(i.getList(), depth-1)
            return ans
        max_depth = depth(nestedList)
        
        return dfs(nestedList, max_depth)

        ## bfscur_level=nestedList
        stack=[]
        
        # bfs
        while cur_level:
            t=0
            next_level=[]
            for element in cur_level:
                if element.isInteger():
                    t+=element.getInteger()
                else:
                    next_level.extend(element.getList())
            cur_level=next_level
            stack.append(t)
            
        # cal. res
        res=0
        for i,n in enumerate(stack[::-1]):
            res+=(i+1)*n
        return res
        