## 第一个是subarray sum，就是求一个数组的所有的subarray的sum的sum，比如[1,2,3]有[1][2][3][1,2][2,3][1,2,3]答案就是1+2+3+(1+2)+(1+3)+(2+3)+(1+2+3)=多少自己算吧


l = len(L)
ans = 0
for i, v in enumerate(L):
	ans += v * (i+1) * (l-i)

return ans