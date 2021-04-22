n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

flag = [False] * 2001

for bit in range(1 << n):
    temp_ans = 0
    for i in range(n):
        if bit & (1 << i):
            temp_ans += A[i]
    flag[temp_ans] = True

for m in M:
    if flag[m]:
        print("yes")
    else:
        print("no")