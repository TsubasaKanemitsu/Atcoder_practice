
n = int(input())
cnt = 0
num = 1
for i in range(1, n + 1):
    n = i
    temp_cnt = 0
    while True:
        ans = n % 2
        if ans != 0:
            break
        n = n // 2
        temp_cnt += 1
    if temp_cnt > cnt:
        num = i
        cnt = temp_cnt

print(num)