n = int(input())
a = list(map(int, input().split()))

a.sort()

if a[0] == 1:
	for i in range(n - 1):
		if a[i + 1] - a[i] == 1:
			pass
		else:
			print("No")
			exit()
	print("Yes")
else:
	print("No")