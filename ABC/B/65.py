n = int(input())

A = []

for i in range(n):
    A.append(int(input()))

count = 0
button = 0
while count <= n:
    if A[button] == 2:
        count += 1
        print(count)
        exit()
    else:
        button = A[button] - 1
        count += 1
print(-1)