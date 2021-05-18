n = int(input())
ST = []
for i in range(n):
    s, t = list(input().split())
    t = int(t)
    ST.append([s, t])
ST.sort(key=lambda x:x[1], reverse=True)
print(ST[1][0])