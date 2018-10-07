## Distinct pairs
## input [1, 46, 46, 1], target = 47
## return 1, cuz (1, 46)

L = [1, 46, 46, 1]
target = 47
dic = {}
ans = 0
for i in L:
	if i in dic and dic[i]:
		continue
	if i not in dic:
		dic[target-i] = False
	else:
		ans += 1
		dic[target-i] = True
		dic[i] = True
return count