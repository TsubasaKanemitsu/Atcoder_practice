l, r = list(map(int, input().split()))
l -= 1
r -= 1
S = input()

ans = S[0:l] + S[l:r + 1][::-1] + S[r + 1:]
print(ans)