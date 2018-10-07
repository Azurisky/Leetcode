## 给你一个整数n, 你被要求返回List<List<Integer>>, 每个 List<Integer> 都由1到n组成并且奇偶相间, 按照"lexicographic order"排好。 例: n = 4. you should return: [[1,2,3,4], [1,4,3,2], [2,1,4,3], [2,3,4,1], [3,2,1,4], [3,4,1,2],
## 3/5
## [4,1,2,3], [4,3,2,1]] 不仅要奇偶相间而且要从小到大排列所有符合的List<Integer>.


l = len(nums)
ans = []
nums = [i+1 for i in range(l)]
print(nums)

def dfs(path, nums):
    if path and len(path) == l:
        ans.append(path)
    for i, v in enumerate(nums):
        if not path:
            dfs(path + [v], nums[:i] + nums[i+1:])
        elif path[-1]%2 == 1 and v%2 == 0:
            dfs(path + [v], nums[:i] + nums[i+1:])
        elif path[-1]%2 == 0 and v%2 == 1:
            dfs(path + [v], nums[:i] + nums[i+1:])
            
dfs([], nums)
return ans