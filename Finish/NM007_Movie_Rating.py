## Movie rating, 不能連續跳過兩個值

## input [9, -1, -3, 4, 5]
## return [9, -1, 4, 5] sum = 17

L = [9, -1, -3, 4, 5]
l = len(L)
get = 0
noget = 0

for i in range(l):
	get, noget = max(noget+i, get+i), get

return max(get, noget)
