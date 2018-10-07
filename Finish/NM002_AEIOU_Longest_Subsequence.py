## 给你一个字符串，由aeiou构成，让你求一个最长的子序列，子序列需要满足：e必须跟在a后面，i必须跟在e后面，... u必须跟在o后面；而且aeiou5个字符都要出现，不存在的话返回0.
## 比如：aeiouaeiou，最长的可以是aaeiou或者aeeiou，返回6。

## aeiou longest subsequence

dp = [[0] * 5] * len(s)

for i, v in enumerate(s):
	if v == 'a':
		dp[i][0] += 1
	elif v == 'e':
		if dp[i][0] > 0 or dp[i][1] > 0:
			dp[i][1] = max(dp[i][0]+1, dp[i][1]+1)
	elif v == 'i':
		if dp[i][1] > 0 or dp[i][2] > 0:
			dp[i][2] = max(dp[i][1]+1, dp[i][2]+1)
	elif v == 'o':
		if dp[i][2] > 0 or dp[i][3] > 0:
			dp[i][3] = max(dp[i][2]+1, dp[i][3]+1)
	elif v == 'u':
		if dp[i][3] > 0 or dp[i][4] > 0:
			dp[i][4] = max(dp[i][3]+1, dp[i][4]+1)
	return dp[-1][-1]