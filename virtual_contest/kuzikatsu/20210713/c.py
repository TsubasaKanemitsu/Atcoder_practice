n = int(input())
A = list(map(int, input().split()))

lft_xor = [A[0]]
rft_xor = [A[-1]]

for i in range(1, n - 1):
    lft_xor.append(lft_xor[i - 1] ^ A[i])
    rft_xor.append(rft_xor[i - 1] ^ A[n - (i + 1)])

ans = []
for i in range(n):
    if i == 0:
        ans.append(rft_xor[-1])
    elif i == n - 1:
        ans.append(lft_xor[-1])
    else:
        ans.append(lft_xor[i - 1] ^ rft_xor[n - (i + 2)])

for a in ans:
    print(a, end=" ")