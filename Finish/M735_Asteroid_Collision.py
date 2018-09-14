class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ## while else, faster
        ans = []
        for new in asteroids:
            # when crash happened
            while ans and new < 0 < ans[-1]:
                # left < right
                if ans[-1] < -new:
                    ans.pop()
                    continue
                # left == right
                elif ans[-1] == -new:
                    ans.pop()
                break
            # no crash
            else:
                ans.append(new)
        return ans
        
        ## pass
        stack = []
        for i, v in enumerate(asteroids):
            if v > 0:
                stack.append(v)
            elif v < 0:
                while True:
                    if not stack or stack[-1] < 0:
                        stack.append(v)
                        break
                    tmp = stack[-1]
                    if tmp + v > 0:
                        break
                    elif tmp + v == 0:
                        stack.pop()
                        break
                    else:
                        stack.pop()
        return stack

            
        