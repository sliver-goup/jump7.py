n = 1
while n <= 100:
	if n % 7 != 0:
		if n // 10 != 7:
			if n % 10 != 7:
				print(n)
	n += 1
