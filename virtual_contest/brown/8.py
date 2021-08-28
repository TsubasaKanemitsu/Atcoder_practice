N, L = list(map(int, input().split()))
S = [input() for _ in range(N)]


S.sort()
ans = ''.join(S)
print(ans)