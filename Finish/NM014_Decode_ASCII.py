## Decode ASCII code
## Input 9797
## output 'aa'
## space => 32
## a-z => 97-122
## A-Z => 65-90


def decodeASCII(s):
	index = 0
	ans = ''
	while index < len(s):
		if s[index] == '1':
			ans += chr(int(s[index:index+3]))
			index += 3
		else:
			ans += chr(int(s[index:index+2]))
			index += 2

	return ans
