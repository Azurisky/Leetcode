## Bitwise sorting
## input [8, 7, 4, 5, 3, 1], (1000, 0111, 0100, 0101, 0011, 0001) -> (1, 3, 1, 2, 2, 1)
## return [1, 4, 8, 3, 5, 7]

L = [8, 7, 4, 5, 3, 1]
dic = {}
for i in L:
	tmp = 0
	while i:
		tmp += 1
		i &= i-1
	dic[tmp] = dic.get(tmp, [])
	dic[tmp].append(i)

ans = []
for i in dic:
	l = dic[i]
	l.sorted()
	ans += l

return ans
		
