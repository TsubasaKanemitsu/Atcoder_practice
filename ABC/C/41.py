n = int(input())
a = list(map(int, input().split()))

aa = []
for i in range(n):
    aa.append([i, a[i]])
aa.sort(key=lambda x:x[1], reverse=True)

for i, num in aa:
    print(i + 1)