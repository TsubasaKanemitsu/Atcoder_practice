n = int(input())

h = list(map(int, input().split()))
count = 0
temp_count = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        temp_count += 1
        count = max(count, temp_count)
    else:
        temp_count = 0
print(count)