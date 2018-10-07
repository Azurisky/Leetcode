## Given a box with W white ball and R red ball
## Here is the rule
## If I draw a white one, put it back and redraw one and throw that out
## If I draw a red one, throw that out
## Write a program which will calculate the probability that the last ball in box is red ball

def calculate(R, W):
	dic = {}

	def check(R, W):
		if R == 1 and W == 0:
			return 1
		elif R == 0 and W == 1:
			return 0
		else:
			if "{}, {}".format(W-1, R) not in dic:
				tmpW = check(R, W-1)
				dic["{}, {}".format(W-1, R)] = tmpW
			else:
				tmpW = dic["{}, {}".format(W-1, R)]

			if "{}, {}".format(W, R-1) not in dic:
				tmpR = check(R-1, W)
				dic["{}, {}".format(W, R-1)] = tmpR
			else:
				tmpR = dic["{}, {}".format(W, R-1)]

			return (W/R+W) ** 2 * tmpW + ((R/R+W) + (W/R+W)*(R/(W+R)) * tmpR
	

	ans = check(R, W)


