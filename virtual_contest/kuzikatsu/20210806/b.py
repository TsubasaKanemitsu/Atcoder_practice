a, b, c = list(map(int, input().split()))
k = int(input())
a, b, c = sorted([a, b, c])
ans = c * 2 ** k + a + b
print(ans)