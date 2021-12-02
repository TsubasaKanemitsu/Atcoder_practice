n, k, q = list(map(int, input().split()))

cnt = [0] * n

for i in range(q):
    a = int(input())
    cnt[a - 1] += 1

for c in cnt:
    if k > (q - c):
        print("Yes")
    else:
        print("No")