n, k = list(input().split())
k = int(k)

def _g1(n):
    if n[0] == '-':
        n = n[1:]
        result = int(''.join(sorted(list(n), reverse=True)))
    else:
        result = int(''.join(sorted(list(n), reverse=True)))
    return result


def _g2(n):
    if n[0] == '-':
        n = n[1:]
        result = - 1 * int(''.join(sorted(list(n))))
        
    else:
        result = int(''.join(sorted(list(n))))
    return result


def f(n):
    result = _g1(n) - _g2(n)
    return result


result = str(n)
for i in range(k):
    result = f(result)
    result = str(result)
print(result)