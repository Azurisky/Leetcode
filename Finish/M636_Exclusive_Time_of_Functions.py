class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        
        if n <= 0:
            return []
        stack = []
        ans = [0] * n
        for i in logs:
            data = i.split(":")
            log_id, action, time = int(data[0]), data[1], int(data[2])
            if action == 'start':
                stack.append([log_id, time, time])
            else:
                tmp = stack.pop()
                original_t, convert_t = tmp[1], tmp[2]
                length = time - convert_t
                ans[log_id] += length + 1
                if stack:
                    stack[-1][2] += time - original_t + 1
        return ans
        