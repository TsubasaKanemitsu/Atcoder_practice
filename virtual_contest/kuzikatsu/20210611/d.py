# https://drken1215.hatenablog.com/entry/2019/03/09/224100

a, b = list(map(int, input().split()))


def f(n):
    if (n // 2) % 2 == 1:
        ans = n ^ 1
    else:
        ans = n ^ 0
    return ans


F_a = f(a - 1)
F_b = f(b)
print(F_a, F_b)
print(F_a ^ F_b)
