N = int(input())

A = list(map(int, input().split()))

result = 0
temp_count = 0
count = 0
for i in range(2, 1001):
    temp_count = 0
    for j in range(N):
        if A[j] % i == 0:
            temp_count += 1
    if temp_count >= count:
        count = temp_count
        result = i

print(result)