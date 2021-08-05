k = int(input())

def divisor(n):
    i = 1
    ans = []
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n//i)
        i += 1
    return ans

A = divisor(k)

ans = 0

for a in A:
    for b in A:
        if a <= b <= k // (a * b) and k % (a * b) == 0:
            ans += 1
print(ans)