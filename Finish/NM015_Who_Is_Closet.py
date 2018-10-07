## Who is closet?
## input s = "babababa", query = [1, 2, 3, 4] => [a, b, a, b]
## output will be a list of index which is closet to this char 
## [3, 0, 1, 2]

def findcloset:
	tmp = [-1 for i in range(26)]
	left = []
	right = []
	for i, v in s:
		left.append(tmp[ord(v)-ord('a')])
		tmp[ord(v)-ord('a')] = i

	tmp = [-1 for i in range(26)]
	for i in range(len(s)-1, -1, -1):
		v = s[i]
		right = [tmp[ord(v)-ord('a')]] + right
		tmp[ord(v)-ord('a')] = i

	ans = []
	for i, v in enumerate(query):
		if left[i] == -1 and right[i] == -1:
			ans.append(-1)
		elif left[i] == -1:
			ans.append(right[i])
		elif right[i] == -1:
			ans.append(left[i])
		else:
			if (i - left[i]) <= (right[i] = i):
				ans.append(left[i])
			else:
				ans.append(right[i])

	return ans






