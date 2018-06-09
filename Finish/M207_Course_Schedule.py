class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        need = [[] for i in range(numCourses)]
        pre_course = [0]*numCourses
        queue = []
        count = 0
        
        for i, j in prerequisites:
            pre_course[i] += 1
            need[j].append(i)
     
        for c in range(numCourses):
            print(pre_course[c], c)
            if pre_course[c] == 0:
                queue.append(c)

        while queue:
            count += 1
            c = queue.pop(0)
            for item in need[c]:
                pre_course[item] -= 1
                if pre_course[item] == 0:
                    queue.append(item)
        
        if count == numCourses:
            return True
        return False