n = int(input())
T = list(map(int, input().split()))
T.sort(reverse=True)
print(T)
a = []
b = []

for i in range(n):
    if sum(a) >= sum(b):
        b.append(T[i])
    else:
        a.append(T[i])
print(max(sum(a), sum(b)))