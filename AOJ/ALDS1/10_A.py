# メモ化最適
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

done = [False] * (n + 1)
fib_n = [0] * (n + 1)


def fib(i):
    if done[i]:
        return fib_n[i]

    if i == 0:
        return 1
    elif i == 1:
        return 1
    else:
        ret = fib(i - 1) + fib(i - 2)
        fib_n[i] = ret
        done[i] = True
    return ret


print(fib(n))