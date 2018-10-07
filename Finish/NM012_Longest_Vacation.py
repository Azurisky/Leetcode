## 是給你一個list
## 裡面有[F, T]
## 然後F代表要上班
## T代表不用上班
## 然後給一個n
## 是代表可以請假幾天
## 問你最長可以放幾天連假

##  [F, F, T, T, F, T, F, F, T] n = 2
## output = 5

def longestVacation(Calender, N):
	left = 0
	right = 0
	ans = 0
	res = 0
	while right < len(Calender):
		if N > 0:
			if Calender[right] == 'F':
				N -= 1
				right += 1
				ans += 1
			else:
				right += 1
				ans += 1
		else:
			if Calender[right] == 'F':
				while Calender[left] != 'F':
					left += 1
					ans -= 1
				N += 1
			else:
				right += 1
				ans += 1
		res = max(res, ans)
	return res
		
