a, b, c = list(map(int, input().split()))

if a >= 0 and b >= 0:
	if a > b:
		print(">")
	elif a < b:
		print("<")
	else:
		print("=")
elif a >= 0 and b < 0:
	if c % 2 == 1:
		print(">")
	else:
		if a > - b:
			print(">")
		elif a < -b:
			print("<")
		else:
			print("=")
elif a < 0 and b >= 0:
	if c % 2 == 1:
		print("<")
	else:
		if - a > b:
			print(">")
		elif - a < b:
			print("<")
		else:
			print("=")
elif a <= 0 and b <= 0:
	if a > b:
		if c % 2 == 0:
			print("<")
		else:
			print(">")
	elif a < b:
		if c % 2 == 0:
			print(">")
		else:
			print("<")
	else:
		print("=")
elif a == 0 and b == 0:
	print("=")