n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]
AB.sort(key=lambda x:x[1])

cnt = 1
st = AB[0][0]
end = AB[0][1]
for i in range(1, n):
    a, b = AB[i]
    if a > end:
        end = b
        cnt += 1
print(cnt)