n = int(input())


def f(n):
    i = 1
    ans = []
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
        i += 1
    return ans


ans = f(n)
sum_ = 0
for a in ans:
    a -= 1
    if a == 0:
        continue
    if n // a == n % a:
        sum_ += a
print(sum_)