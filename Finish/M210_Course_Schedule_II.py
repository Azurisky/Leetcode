class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        require = [[] for i in range(numCourses)]
        pre_course = [0 for i in range(numCourses)]
        queue = []
        ans = []
        for i, j in prerequisites:
            require[j].append(i)
            pre_course[i] += 1
        
        for i in range(numCourses):
            if pre_course[i] == 0:
                queue.append(i)
            
        while queue:
            c = queue.pop(0)
            ans.append(c)
            for i in require[c]:
                pre_course[i] -= 1
                if pre_course[i] == 0:
                    queue.append(i)
        
        if len(ans) == numCourses:
            return ans
        return []