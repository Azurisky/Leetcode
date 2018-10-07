## 1. Email处理。 email地址分为local@domain。（1）local里dots('.') between some characters 要去除。（2）local里如果有'+'，'+'和后面的全去除。比如'a.b@example.com' -> 'ab@example.com', 'dupli......cate@example.com' -> 'duplicate@example.com',  'd.u.p.l.i.c.a.t.e@example.com' -> 'duplicate@example.com',  'ab+work@example.com' -> 'ab@example.com'。处理完后的邮件地址一样的放在一组，返回所有组，里面不止一个邮件地址的组的个数。	来源一亩.三分地论坛. 

dic = {}
for email in L:
	new = email
	tmp = new.split("@")
	local = tmp[0]
	domain = tmp[1]


	first = 0
	while first < len(local)-1:
		if local[first] == '.':
			first += 1
		else:
			break

	last = len(local)-1
	while last > first:
		if local[last] == '.':
			last -= 1
		else:
			break

	count = first
	while count <= last:
		if local[count] == '.':
			local = local[:count] + local[count+1:]
			last -= 1

	local = local.split("+")[0]
	key = local + "@" + domain

	dic[key] = dic.get(key, [])
	dic[key].append(email)
ans = 0
for i in dic:
	if len(dic[i]) > 1:
		ans += 1

return ans
