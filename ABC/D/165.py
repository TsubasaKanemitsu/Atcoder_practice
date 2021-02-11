a, b, n = list(map(int, input().split()))


def floor(A, X, B):
    result = A * X // B
    return result


if n >= b:
    x = b - 1
else:
    x = n

ans = floor(a, x, b) - a * (x // b)
print(ans)