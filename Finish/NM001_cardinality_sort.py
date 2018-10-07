## https://www.geeksforgeeks.org/sort-array-according-count-set-bits/

## cardinality sort

dic = {}
l = []
ans = []
for i in nums:
	count = 0
	while i:
		i = i and (i-1)
		count += 1
	dic[count] = dic.get(count, [])
	dic[count].append(i)
	if count not in l:
		l.append(count)

l.sorted()
for i in l:
	ans.append(dic[i])

return ans
	