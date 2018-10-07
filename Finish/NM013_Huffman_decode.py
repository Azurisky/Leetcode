## Huffman Code compress string

# '100101' - > a
# '100100' - > b

def decode(S, L):
	dic = {}
	for i, j in L:
		l = len(i)
		dic[l] = dic.get(l, {})
		dic[l][i] = j

	start = 0
	ans = []
	for i, v in enumerate(S):
		l = i-start
		if l in dic and S[start:i+1] in dic[l]:
			ans.append(S[start:i+1])
			start = i+1
			continue
		else:
			continue

	return ans
