n = int(input())

ans = 10 ** 99

AB = [list(map(int, input().split())) for _ in range(n)]

a_time = 10 ** 99
b_time = 10 ** 99
common = 10 ** 99
for i in range(n):
    a = AB[i][0]
    b = AB[i][1]

    diff_a = a_time - a
    diff_b = b_time - b
    if diff_a >= diff_b:
        a_time = min(a, a_time)
    else:
        b_time = min(b, b_time)
    common = min(common, a + b)
print(min(max(a_time, b_time), common))