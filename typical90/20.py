a, b, c = list(map(int, input().split()))
bc = 1
for i in range(b):
    bc *= c

if a < bc:
    print("Yes")
else:
    print("No")