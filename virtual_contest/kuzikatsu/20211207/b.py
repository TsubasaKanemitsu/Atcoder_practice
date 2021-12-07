n = int(input())
T = list(map(int, input().split()))
m = int(input())

sum_t = sum(T)
ans = []
for i in range(m):
    p, x = list(map(int, input().split()))
    ans.append(sum_t - (T[p - 1] - x))

for a in ans:
    print(a)