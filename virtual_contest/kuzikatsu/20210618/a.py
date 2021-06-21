n = int(input())
ST = [list(input().split()) for _ in range(n)]

for i in range(n):
    s, t = ST[i]
    ST[i] = [s, int(t)]

ST.sort(key=lambda x:x[1], reverse=True)
print(ST[1][0])
